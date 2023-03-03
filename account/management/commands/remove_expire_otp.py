from django.core.management.base import BaseCommand
from account.models import OtpCode
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'remove all expire otp codes'

    def handle(self, *args, **options):
        expire_time = datetime.now() - timedelta(minutes=4)
        print(expire_time)
        OtpCode.objects.filter(created__lt=expire_time).delete
        self.stdout.write('all expired OTP codes deleted')
