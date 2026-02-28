"""Test settings - uses SQLite for fast tests without PostgreSQL."""
from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Simpler static storage for tests (no manifest required)
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
