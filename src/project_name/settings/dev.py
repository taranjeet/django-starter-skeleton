# *-* coding: utf-8 -*-

from .common import *       # noqa

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="todo-set-new-secret-key-here",
)

DEBUG = True
