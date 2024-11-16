from django.core.management.base import BaseCommand
from django.utils import timezone
from library.models import BookIssue

class Command(BaseCommand):
    help = 'Cancel book reservations older than 1 day'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        expired_reservations = BookIssue.objects.filter(return_date=None, is_returned=False, issue_date__lt=today)
        expired_reservations.update(is_returned=True)
        self.stdout.write(self.style.SUCCESS('Successfully canceled expired reservations'))
