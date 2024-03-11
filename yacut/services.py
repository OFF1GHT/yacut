import re
from random import choice
from string import ascii_letters, digits

from flask import url_for

from .models import URLMap
from . import db
from .error_handlers import MissingRequiredParameterError, ValidationError
from .constants import MIN_SHORT_LINK_LENGTH, SHORT_ID_VALIDATION_REGEX


class URL:
    def __init__(self, url=None, custom_id=None):
        self.custom_id = custom_id
        self.url = url

    def get_url(self, short_id=None):
        return URLMap.query.filter_by(
            short=short_id if short_id else self.custom_id
        ).first()

    def create_short_link(self):
        if not self.url:
            raise MissingRequiredParameterError()

        if self.custom_id:
            self.validate_custom_id()
        else:
            self.generate_unique_short_id()

        new_url_object = URLMap(original=self.url, short=self.custom_id)
        db.session.add(new_url_object)
        db.session.commit()

        return url_for('redirect_view', id=self.custom_id, _external=True)

    def validate_custom_id(self):
        if self.custom_id is None or not re.fullmatch(SHORT_ID_VALIDATION_REGEX, self.custom_id):
            raise ValidationError()

    def generate_unique_short_id(self):
        self.custom_id = self.generate_short_id()
        while self.get_url():
            self.custom_id = self.generate_short_id()

    @staticmethod
    def generate_short_id():
        chars = ascii_letters + digits
        return ''.join(choice(chars) for _ in range(MIN_SHORT_LINK_LENGTH))