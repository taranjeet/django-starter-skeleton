from django.utils.crypto import get_random_string


def get_short_id(length=8):
    return get_random_string(length).lower()