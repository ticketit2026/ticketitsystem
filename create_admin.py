from django.contrib.auth import get_user_model

User = get_user_model()

import sys
from django.core.management import call_command

if not User.objects.filter(username='admin').exists():
    print("در حال ساخت کاربر ادمین...")
    call_command('createsuperuser', '--noinput', username='admin', email='')
    print("✅ کاربر ادمین ساخته شد")
else:
    print("✅ ادمین قبلاً وجود دارد")
