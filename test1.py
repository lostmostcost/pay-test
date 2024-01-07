import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
from django import setup
setup()

from django.contrib.auth import logout
from dutchpay.models import Event, Member, Pay, Remit
from users.models import CustomUser

def Create_User(user) :
    pw = '12345'

    signIn = CustomUser.objects.create_user(
        username=user[0], 
        password=pw,
        first_name=user[1],
        last_name=user[2],
        bank_account = user[3]
    )

def Create_Event(event):
    Event.objects.create(
        subject=event[0],
    )

def Create_Member(user, event):
    Member.objects.create(
        user=CustomUser.objects.get(username=user[0]),
        event=Event.objects.get(subject=event[0]),
    )

def Create_Pay(pay) :
    Pay.objects.create(
        event=Event.objects.get(subject=event[0]),
        subject=pay[1],
    )

users = [
    ('이문찬', '문찬', '이', '3521327259453 NH농협'),
    ('이지민', '지민', '이', '3521327259453 NH농협'),
    ('김유민', '유민', '김', '3521327259453 NH농협'),
    ('안상현', '상현', '안', '3521327259453 NH농협'),
    ('서민주', '민주', '서', '3521327259453 NH농협'),
    ('김시은', '시은', '김', '3521327259453 NH농협'),
    ('이효림', '효림', '이', '3521327259453 NH농협'),
]

events = [
    ('금강산 3차 회식'),
]

pays = [
    ('금강산 3차 회식', '1차닭갈비', 64000, '이문찬', ('이문찬','이지민','김유민','안상현','서민주','김시은','이효림'))
]

for user in users :
    Create_User(user)
'''

event1 = Event.objects.get(id=1)

event1.settle_payments()
event1.make_bills()
'''

print("hello world")