import re

def validate_email(email: str) -> bool:
    email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    if re.match(email_regex, email):
        return True
    return False
