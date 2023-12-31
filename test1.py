import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
from django import setup
setup()

from django.contrib.auth import logout
from dutchpay.models import CustomUser, Event, Member, Pay, Remit

def Create_User(user) :
    pw = '12345'

    signIn = CustomUser.objects.create_user(
        username=user[0], 
        password=pw,
        first_name=user[1],
        last_name=user[2],
        bank_account = user[3]
    )
    logout(signIn)

users = [
    ('이문찬', '문찬', '이', '01036930521'),
    ('이지민', '지민', '이', '01034368788'),
    ('김유민', '유민', '김', '01038948897'),
    ('안상현', '상현', '안', '01048928932'),
    ('서민주', '민주', '서', '01075809374'),
    ('김시은', '시은', '김', '01034768794'),
    ('이효림', '효림', '이', '01037680789'),
]

'''
for user in users :
    Create_User(user)
'''
event1 = Event.objects.get(id=1)

event1.settle_payments()
event1.make_bills()