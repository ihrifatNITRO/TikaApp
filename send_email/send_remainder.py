from django.core.management.base import BaseCommand
from django.utils import timezone
from .models import ChildInfo
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Send vaccine reminders to parents'

    def handle(self, *args, **options):
        # Calculate the date (1 day before the next_vaccine date)
        current_date = timezone.now().date()
        reminder_date = current_date + timezone.timedelta(days=1)

        # Query ChildInfo records with a next_vaccine date = the reminder date
        children_to_remind = ChildInfo.objects.filter(next_vaccine=reminder_date)

        # Send reminders
        for child in children_to_remind:
            parent_email = child.parent_nid.email
            subject = 'Vaccine Reminder'
            message = f'Dear parent, please remember that your child needs a vaccine tomorrow.'
            from_email = 'ihr@email.com' 
            send_mail(subject, message, from_email, [parent_email])

        self.stdout.write(self.style.SUCCESS('Vaccine reminders sent successfully.'))
