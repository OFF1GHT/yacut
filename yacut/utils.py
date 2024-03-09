import random
import string

from .models import URLMap


def get_unique_short_id(length=6):
    characters = string.ascii_letters + string.digits
    short_id = ''.join(random.choice(characters) for _ in range(length))
    existing_url = URLMap.query.filter_by(short=short_id).first()

    while existing_url:
        short_id = ''.join(random.choice(characters) for _ in range(length))
        existing_url = URLMap.query.filter_by(short=short_id).first()

    return short_id
