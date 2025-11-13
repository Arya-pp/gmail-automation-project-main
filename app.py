from flask import Flask, render_template, jsonify, request
from gmail_automation import get_unread_emails, mark_as_read, mark_as_unread
from email_summarizer import summarize_emails
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/fetch-emails', methods=['GET'])
def fetch_emails():
    """API endpoint to fetch emails with pagination and search"""
    try:
        # Get query parameters
        max_results = int(request.args.get('max_results', 10))
        page_token = request.args.get('page_token', None)
        search_query = request.args.get('q', 'is:unread')
        
        result = get_unread_emails(
            max_results=max_results,
            page_token=page_token,
            search_query=search_query
        )
        
        emails = result.get('emails', [])
        
        if not emails:
            return jsonify({
                'success': True,
                'message': 'No emails found',
                'emails': [],
                'next_page_token': None,
                'total_results': 0
            })
        
        return jsonify({
            'success': True,
            'message': f'Found {len(emails)} emails',
            'emails': emails,
            'next_page_token': result.get('next_page_token'),
            'total_results': result.get('total_results', 0)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error fetching emails: {str(e)}',
            'emails': [],
            'next_page_token': None,
            'total_results': 0
        }), 500

@app.route('/api/summarize-emails', methods=['POST'])
def api_summarize_emails():
    """API endpoint to summarize emails"""
    try:
        data = request.get_json()
        emails = data.get('emails', [])
        
        if not emails:
            return jsonify({
                'success': False,
                'message': 'No emails provided for summarization'
            }), 400
        
        # Check if Gemini API key is set
        if not os.getenv('GEMINI_API_KEY'):
            return jsonify({
                'success': False,
                'message': 'Gemini API key not configured. Please set GEMINI_API_KEY in .env file'
            }), 400
        
        summarized_emails = summarize_emails(emails)
        
        return jsonify({
            'success': True,
            'message': 'Emails summarized successfully',
            'emails': summarized_emails
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error summarizing emails: {str(e)}'
        }), 500

@app.route('/api/check-config', methods=['GET'])
def check_config():
    """Check if configuration is complete"""
    config_status = {
        'gemini_api_key': bool(os.getenv('GEMINI_API_KEY')),
        'credentials_file': os.path.exists('credentials.json'),
        'token_file': os.path.exists('token.json')
    }
    
    all_configured = all(config_status.values())
    
    return jsonify({
        'success': True,
        'configured': all_configured,
        'status': config_status,
        'message': 'All configured!' if all_configured else 'Configuration incomplete'
    })

@app.route('/api/mark-read', methods=['POST'])
def mark_read():
    """Mark emails as read"""
    try:
        data = request.get_json()
        email_ids = data.get('email_ids', [])
        
        if not email_ids:
            return jsonify({
                'success': False,
                'message': 'No email IDs provided'
            }), 400
        
        result = mark_as_read(email_ids)
        
        return jsonify(result)
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error marking emails as read: {str(e)}'
        }), 500

@app.route('/api/mark-unread', methods=['POST'])
def mark_unread():
    """Mark emails as unread"""
    try:
        data = request.get_json()
        email_ids = data.get('email_ids', [])
        
        if not email_ids:
            return jsonify({
                'success': False,
                'message': 'No email IDs provided'
            }), 400
        
        result = mark_as_unread(email_ids)
        
        return jsonify(result)
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error marking emails as unread: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
