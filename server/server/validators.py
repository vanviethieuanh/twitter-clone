from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, RegexValidator
from django.contrib.auth.models import User

def validate_register(data):
    password = data['password']
    email = data['email']

    EmailValidator()(email)
    
    if min(1, User.objects.filter(email=email).count()):
        raise ValidationError(
            'An account with this email address already exists.',
        )
