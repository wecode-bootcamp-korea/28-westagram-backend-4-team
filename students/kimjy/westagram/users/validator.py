import re

def validate_email(character:str):

    if not re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', character):
        raise KeyError('INVALID_EMAIL_ADDRESS')

def validate_password(character:str):

    if not re.match(
            "((?=.*[0-9])(?=.*[a-z|A-Z])(?=.*[`~!@#$%^&*\(\)-_=+\\\|;:\'\",<.>\/?]).{8,})" ,
            character):
        raise KeyError('INVALID_PASSWORD')

