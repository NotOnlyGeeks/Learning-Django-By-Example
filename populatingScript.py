import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Learning_Django_By_Example.settings')

import django
django.setup()

import random
from app7.models import Users
from faker import Faker

fakegen = Faker()

def add_user(N=5):

    for i in range(N):
        firstName=fakegen.first_name()
        lastName=fakegen.last_name()
        email=fakegen.email()

        t = Users.objects.get_or_create(FirstName=firstName,LastName=lastName,Email=email)[0]
        t.save()

if __name__=='__main__':
    add_user(20)

