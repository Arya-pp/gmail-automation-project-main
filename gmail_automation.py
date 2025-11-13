import os.path
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from bs4 import BeautifulSoup

# If modifying these SCOPES, delete the token.json file
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.modify'  # Added for mark as read/unread
]

def get_unread_emails(max_results=10, page_token=None, search_query="is:unread"):
    """Fetch unread email snippets from Gmail with pagination and search support
    
    Args:
        max_results: Number of emails to fetch (default 10)
        page_token: Token for pagination (get next page)
        search_query: Gmail search query (default "is:unread")
    
    Returns:
        dict: {
            'emails': list of email dicts,
            'next_page_token': token for next page (None if no more),
            'total_results': estimated total results
        }
    """
    try:
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        service = build('gmail', 'v1', credentials=creds)

        # Fetch messages with pagination
        results = service.users().messages().list(
            userId='me',
            labelIds=['INBOX'],
            q=search_query,
            maxResults=max_results,
            pageToken=page_token
        ).execute()
        
        messages = results.get('messages', [])
        next_page_token = results.get('nextPageToken')
        result_size = results.get('resultSizeEstimate', 0)

        if not messages:
            return {
                'emails': [],
                'next_page_token': None,
                'total_results': 0
            }

        emails = []
        for msg in messages:
            try:
                msg_data = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
                payload = msg_data['payload']
                headers = msg_data['payload']['headers']
                
                subject = next((header['value'] for header in headers if header['name'] == 'Subject'), '(No Subject)')
                sender = next((header['value'] for header in headers if header['name'] == 'From'), '(Unknown)')
                date = next((header['value'] for header in headers if header['name'] == 'Date'), '(No Date)')
                
                # Get email labels to determine read/unread status
                labels = msg_data.get('labelIds', [])
                is_unread = 'UNREAD' in labels
                
                # Extract category (if available)
                category = 'inbox'
                if 'CATEGORY_SOCIAL' in labels:
                    category = 'social'
                elif 'CATEGORY_PROMOTIONS' in labels:
                    category = 'promotions'
                elif 'CATEGORY_UPDATES' in labels:
                    category = 'updates'
                elif 'CATEGORY_FORUMS' in labels:
                    category = 'forums'
                
                body = extract_email_body(payload)
                
                emails.append({
                    'id': msg['id'],
                    'subject': subject,
                    'from': sender,
                    'date': date,
                    'body': body.strip() if body else '(No content available)',
                    'is_unread': is_unread,
                    'category': category
                })
            except Exception as e:
                print(f"Error processing email {msg.get('id', 'unknown')}: {e}")
                continue

        return {
            'emails': emails,
            'next_page_token': next_page_token,
            'total_results': result_size
        }
    except FileNotFoundError as e:
        print(f"Error: credentials.json file not found. {e}")
        return {'emails': [], 'next_page_token': None, 'total_results': 0}
    except HttpError as error:
        print(f"An HTTP error occurred: {error}")
        return {'emails': [], 'next_page_token': None, 'total_results': 0}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {'emails': [], 'next_page_token': None, 'total_results': 0}

def extract_email_body(payload):
    """Extract email body from payload with better handling for different formats"""
    body = ''
    
    # Check if body data is directly available
    if payload.get('body') and payload['body'].get('data'):
        try:
            body = base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8')
            return clean_html_content(body)
        except Exception as e:
            print(f"Error decoding body data: {e}")
    
    # Check parts for multipart emails
    parts = payload.get('parts', [])
    for part in parts:
        mime_type = part.get('mimeType', '')
        
        # Prefer plain text over HTML
        if mime_type == 'text/plain' and part.get('body', {}).get('data'):
            try:
                data = part['body']['data']
                body = base64.urlsafe_b64decode(data).decode('utf-8')
                return body
            except Exception as e:
                print(f"Error decoding plain text part: {e}")
                continue
        
        # Fallback to HTML if no plain text found
        elif mime_type == 'text/html' and part.get('body', {}).get('data') and not body:
            try:
                data = part['body']['data']
                html_body = base64.urlsafe_b64decode(data).decode('utf-8')
                body = clean_html_content(html_body)
            except Exception as e:
                print(f"Error decoding HTML part: {e}")
                continue
        
        # Handle nested parts
        elif part.get('parts'):
            nested_body = extract_email_body(part)
            if nested_body and not body:
                body = nested_body
    
    return body

def clean_html_content(html_content):
    """Clean HTML content and extract plain text"""
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove script, style, and other unwanted elements
        for element in soup(["script", "style", "meta", "link", "noscript"]):
            element.extract()
        
        # Remove tracking links and buttons (keep link text but remove URLs)
        for link in soup.find_all('a'):
            link_text = link.get_text().strip()
            # Only keep meaningful link text, skip long URLs
            if link_text and len(link_text) < 100 and not link_text.startswith('http'):
                link.replace_with(link_text)
            else:
                link.replace_with('')  # Remove tracking links
        
        # Get text and clean up whitespace
        text = soup.get_text(separator='\n')
        
        # Clean up excessive whitespace and empty lines
        lines = []
        for line in text.splitlines():
            line = line.strip()
            
            # Skip lines that are just URLs or very long tracking links
            if line.startswith('http://') or line.startswith('https://'):
                continue
            
            # Skip very long lines (usually tracking URLs)
            if line and len(line) < 500:
                # Remove excessive dashes
                if not (line.count('-') > 10 and len(line) < 50):
                    lines.append(line)
        
        # Remove duplicate consecutive lines
        cleaned_lines = []
        prev_line = None
        for line in lines:
            if line != prev_line:
                cleaned_lines.append(line)
                prev_line = line
        
        # Join and limit to reasonable length
        result = '\n'.join(cleaned_lines)
        
        # Remove inline URLs from remaining text (more aggressive)
        import re
        # Remove full URLs
        result = re.sub(r'https?://[^\s]+', '', result)
        # Remove URL fragments and tracking parameters
        result = re.sub(r'lipi=urn[^\s]+', '', result)
        result = re.sub(r'midToken=[^\s]+', '', result)
        result = re.sub(r'trk=[^\s]+', '', result)
        result = re.sub(r'trkEmail=[^\s]+', '', result)
        result = re.sub(r'&[a-zA-Z]+=[^\s]+', '', result)
        
        # Remove lines that are mostly URL parameters
        lines = result.split('\n')
        clean_lines = []
        for line in lines:
            # Skip lines with URL-like patterns
            if not re.search(r'[?&=]{3,}|%[0-9A-F]{2}|utm_|lipi|midToken', line):
                clean_lines.append(line)
        
        result = '\n'.join(clean_lines)
        
        # Remove excessive blank lines
        result = re.sub(r'\n{3,}', '\n\n', result)
        
        # Truncate very long emails
        if len(result) > 2000:
            result = result[:2000] + '\n\n... (Email truncated for readability)'
        
        return result.strip()
    except Exception as e:
        print(f"Error cleaning HTML content: {e}")
        # Fallback: try basic text extraction
        try:
            return html_content[:500] + '...'
        except:
            return html_content

def mark_as_read(email_ids):
    """Mark emails as read
    
    Args:
        email_ids: List of email IDs or single email ID string
    
    Returns:
        dict: {'success': bool, 'message': str, 'modified_count': int}
    """
    try:
        # Handle single email ID
        if isinstance(email_ids, str):
            email_ids = [email_ids]
        
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                return {'success': False, 'message': 'Authentication required', 'modified_count': 0}
        
        service = build('gmail', 'v1', credentials=creds)
        
        modified_count = 0
        for email_id in email_ids:
            try:
                service.users().messages().modify(
                    userId='me',
                    id=email_id,
                    body={'removeLabelIds': ['UNREAD']}
                ).execute()
                modified_count += 1
            except Exception as e:
                print(f"Error marking email {email_id} as read: {e}")
                continue
        
        return {
            'success': True,
            'message': f'Marked {modified_count} email(s) as read',
            'modified_count': modified_count
        }
    except Exception as e:
        return {
            'success': False,
            'message': f'Error: {str(e)}',
            'modified_count': 0
        }

def mark_as_unread(email_ids):
    """Mark emails as unread
    
    Args:
        email_ids: List of email IDs or single email ID string
    
    Returns:
        dict: {'success': bool, 'message': str, 'modified_count': int}
    """
    try:
        # Handle single email ID
        if isinstance(email_ids, str):
            email_ids = [email_ids]
        
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                return {'success': False, 'message': 'Authentication required', 'modified_count': 0}
        
        service = build('gmail', 'v1', credentials=creds)
        
        modified_count = 0
        for email_id in email_ids:
            try:
                service.users().messages().modify(
                    userId='me',
                    id=email_id,
                    body={'addLabelIds': ['UNREAD']}
                ).execute()
                modified_count += 1
            except Exception as e:
                print(f"Error marking email {email_id} as unread: {e}")
                continue
        
        return {
            'success': True,
            'message': f'Marked {modified_count} email(s) as unread',
            'modified_count': modified_count
        }
    except Exception as e:
        return {
            'success': False,
            'message': f'Error: {str(e)}',
            'modified_count': 0
        }

# Test function to run the email fetcher
if __name__ == "__main__":
    print("Fetching unread emails...")
    emails = get_unread_emails()
    
    if emails:
        print(f"\nFound {len(emails)} unread emails:\n")
        for i, email in enumerate(emails, 1):
            print(f"--- Email {i} ---")
            print(f"From: {email['from']}")
            print(f"Subject: {email['subject']}")
            print(f"Date: {email['date']}")
            print(f"Body: {email['body'][:200]}...")  # First 200 characters
            print("-" * 50)
    else:
        print("No unread emails found or an error occurred.")
