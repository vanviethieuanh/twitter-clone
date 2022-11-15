from django.core.management.base import BaseCommand
from authentication.models import User

import random
import names


class Command(BaseCommand):
    help = 'Seed data to database.'

    def add_arguments(self, parser):
        parser.add_argument('amount', nargs='+', type=int)

    def handle(self, *args, **options):
        amount = options['amount'][0]
        for _ in range(amount):
            create_user()


def create_user():
    gender = 'male' if (random.random() > 0.5) else 'female'

    first_name = names.get_first_name(gender=gender)
    last_name = names.get_last_name()
    email = f'{first_name.lower()}_{last_name.lower()}_{random.randint(1,1000)}@gmail.com'
    username = f'{first_name.lower()}{last_name.lower()}{random.randint(1,1000)}'

    user = User(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name
    )
    user.set_password('123123123')
    user.save()
