import os
import google.generativeai as genai
from gmail_automation import get_unread_emails
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def initialize_gemini_client():
    """Initialize Gemini client with proper error handling"""
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key or api_key == 'your_gemini_api_key_here':
        print("❌ Gemini API key not found or not set!")
        print("Please follow these steps:")
        print("1. Get your API key from: https://makersuite.google.com/app/apikey")
        print("2. Edit the .env file and replace 'your_gemini_api_key_here' with your actual API key")
        print("3. Or enter it manually below:")
        
        api_key = input("Enter your Gemini API key: ").strip()
        if not api_key:
            raise ValueError("Gemini API key is required to run this script.")
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash')
        return model
    except Exception as e:
        raise ValueError(f"Failed to initialize Gemini client: {str(e)}")

# Initialize Gemini client with error handling
try:
    model = initialize_gemini_client()
except ValueError as e:
    print(f"Error: {e}")
    model = None

def summarize_email(text):
    """Summarize email content using Google Gemini"""
    if not text or text.strip() == '':
        return "No content to summarize."
    
    if not model:
        return "Gemini API not configured"
    
    try:
        prompt = f"Summarize this email in 2-3 sentences:\n\n{text}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error summarizing email: {str(e)}"

def summarize_emails(emails):
    """Summarize multiple emails using Gemini API (for web app)"""
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key or api_key == 'your_gemini_api_key_here':
        raise ValueError("Gemini API key not configured")
    
    try:
        genai.configure(api_key=api_key)
        gemini_model = genai.GenerativeModel('gemini-2.0-flash')
        
        for email in emails:
            # Skip if already summarized
            if 'summary' in email and email['summary']:
                continue
            
            email_body = email.get('body', '')[:2000]  # Limit length
            prompt = f"Summarize this email in 2-3 sentences:\n\nSubject: {email['subject']}\n\n{email_body}"
            
            try:
                response = gemini_model.generate_content(prompt)
                email['summary'] = response.text.strip()
            except Exception as e:
                email['summary'] = f"Error: {str(e)}"
        
        return emails
    except Exception as e:
        raise ValueError(f"Failed to summarize emails: {str(e)}")

def main():
    """Main function to fetch and summarize emails"""
    print("🔍 Fetching unread emails...")
    emails = get_unread_emails()
    
    if not emails:
        print("❌ No unread emails found or error occurred.")
        return
    
    print(f"📬 Found {len(emails)} unread emails\n")
    
    for i, email in enumerate(emails, 1):
        print(f"📧 Email #{i}")
        print(f"From: {email['from']}")
        print(f"Subject: {email['subject']}")
        print(f"Date: {email.get('date', 'No date')}")
        print("Summary:")
        
        # Limit email body length for summarization
        email_body = email.get('body', '')
        if len(email_body) > 2000:
            email_body = email_body[:2000] + "..."
            
        summary = summarize_email(email_body)
        print(f"  {summary}")
        print("-" * 60)

if __name__ == "__main__":
    main()
