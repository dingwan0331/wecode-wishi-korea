import re

from django.core.exceptions import ValidationError

def validate_names(username, nick_name, last_name, first_name):
    USERNAME_REGEX  = '^[가-힣a-zA-Z0-9]+$'
    NICK_NAME_REGEX = '^[가-힣a-zA-Z0-9]*$'
    NAMES_REGEX     = '^[가-힣a-zA-Z]+$'

    if not re.match(USERNAME_REGEX, username):
        raise ValidationError(message = 'Invalid Username')

    if not re.match(NICK_NAME_REGEX, nick_name):
        raise ValidationError(message = 'Invalid Nick Name')
    
    if not re.match(NAMES_REGEX, last_name):
        raise ValidationError(message = 'Invalid Last Name')
    
    if not re.match(NAMES_REGEX, first_name):
        raise ValidationError(message = 'Invalid First Name')

def validate_email(value):
    EMAIL_REGEX  = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if not re.match(EMAIL_REGEX, value):
        raise ValidationError(message = 'Invalid Email')
        
def validate_password(value):
    PASSWORD_REGEX = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'

    if not re.match(PASSWORD_REGEX, value):
        raise ValidationError(message = 'Invalid Password')

def validate_phone_number(value):
    PHONE_NUMBER_REGEX  = '\d{3}-\d{3,4}-\d{4}'

    if not re.match(PHONE_NUMBER_REGEX ,value):
        raise ValidationError(message = 'Invalid PhoneNumber')