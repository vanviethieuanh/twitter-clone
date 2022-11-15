from django.core.management.base import BaseCommand
from authentication.models import User
from twitter.models import Follow


class Command(BaseCommand):
    help = 'Seed data to database.'

    def add_arguments(self, parser):
        parser.add_argument('amount', nargs='+', type=int)

    def handle(self, *args, **options):
        amount = options['amount'][0]
        for _ in range(amount):
            create_follow(User.objects.order_by('?').first(),
                          User.objects.order_by('?').first())


def create_follow(follower, following):
    follow = Follow(
        follower=follower,
        following=following
    )
    follow.save()
