def sanitize_input(user_input):
    """Basic input sanitization"""
    return user_input.strip()

def format_string(template, **kwargs):
    """Format string with variables"""
    return template.format(**kwargs)
