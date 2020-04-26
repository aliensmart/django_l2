import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1.settings')

import django
django.setup()



#Faker
import random
from firstapp.models import AccessRecord, Topic, Webpage
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0] #retrieve the topic or create it if it does exist
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        #get topic for the entry
        top = add_topic()

        #create the fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the new webpage
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        #Create fake Access record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)


if __name__=='__main__':
    print('Populating script!')
    populate(20)
    print('Populating complete')