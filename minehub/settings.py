from pathlib import Path
import os

import os


SECRET_KEY = '!&#b(^zox!(x3u)&#n-12n9anthv#@vt&9t6mu+33+!*gtwuca'

MEDIA_URL = '/media/'
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_ROOT = BASE_DIR / 'media'



APPEND_SLASH = False

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Static files (CSS, JavaScript, Images)


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    # your apps
    'rest_framework',
    'equipment',
    'jobs',
    'training',
    'users',
]

ROOT_URLCONF = 'minehub.urls'


DEBUG = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # or your custom template folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # REQUIRED
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # REQUIRED
    'django.contrib.messages.middleware.MessageMiddleware',     # REQUIRED
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',   # <--- This is the ENGINE Django expects!
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


ALLOWED_HOSTS = ['*']


# CORS headers
INSTALLED_APPS += ['corsheaders']
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

CORS_ALLOW_ALL_ORIGINS = True
