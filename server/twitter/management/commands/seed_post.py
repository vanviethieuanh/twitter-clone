from django.core.management.base import BaseCommand
from authentication.models import User
from twitter.models import Post

import lorem


class Command(BaseCommand):
    help = 'Seed data to database.'

    def add_arguments(self, parser):
        parser.add_argument('amount', nargs='+', type=int)

    def handle(self, *args, **options):
        amount = options['amount'][0]
        for _ in range(amount):
            create_post(User.objects.order_by('?').first())


def create_post(author):
    post = Post(
        post=lorem.sentence(),
        author=author
    )
    post.save()
