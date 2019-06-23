import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Learning_Django_By_Example.settings')

import django
django.setup()

import random
from app5.models import Topic,AccessRecord,Webpage
from faker import Faker

fakegen = Faker()

topics = ['Health Care','News','Games','Search']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choices(topics)[0])[0]
    t.save()
    return t

def generate(N=5):

    for i in range(N):
        t = add_topic()

        name = fakegen.company()
        url = fakegen.url()
        date = fakegen.date()

        w = Webpage.objects.get_or_create(topic = t,name=name,url=url)[0]
        w.save()

        a = AccessRecord.objects.get_or_create(name=w,date=date)[0]
        a.save()


if __name__=='__main__':
    generate(20)
