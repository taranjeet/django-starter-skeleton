# *-* coding: utf-8 -*-

import os
from .common import *       # noqa

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT_DIR, 'db.sqlite3'),       # noqa
    }
}
