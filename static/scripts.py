from datetime import datetime

def format_blog_post(title, content):
    """Format a blog post with a timestamp."""
    return {
        'title': title,
        'content': content,
        'date': datetime.now().strftime('%B %d, %Y')
    }

def validate_contact_form(name, email, message):
    """Validate contact form input."""
    errors = []
    if not name.strip():
        errors.append("Name is required.")
    if not email.strip() or '@' not in email:
        errors.append("Valid email is required.")
    if not message.strip():
        errors.append("Message is required.")
    return errors