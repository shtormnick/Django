import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoPro3.settings')

import django
django.setup()

# Fake populat script
import random
from first_app.models import User
from faker import Faker

fgen = Faker()


def populate(N=5):
    for entery in range(N):
        fake_fname = fgen.name().split()[0]
        fake_lname = fgen.name().split()[1]
        fake_email = fgen.email()

        try:
            users = User.objects.get_or_create(email=fake_email,
                                            first_name=fake_fname,
                                                last_name=fake_lname)[0]
        except Exception:
            pass
if __name__ == '__main__':
    print('population script has been started!')
    populate(20)
    print('population script finished!')
