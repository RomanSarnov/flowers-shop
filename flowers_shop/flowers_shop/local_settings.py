import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '3xw$wnvhaby0#(olv@o%-78r-w00@p1!k^v3@f23qy()cgenqn'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]
