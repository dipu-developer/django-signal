from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User

def login_sucess(sender,reqeust,user,**kwargs):
    print('--------------------------------')
    print("Logged in Siginal ...")
    print('Sender:', sender)
    print('Request:', reqeust)
    print('User:', user)
    print(f'kwargs: {kwargs}')

    user_logged_in.connect(login_sucess,sender=User)
    