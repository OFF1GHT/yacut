from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp

from .constants import MAX_SHORT_LINK_LENGTH, SHORT_ID_VALIDATION_REGEX


class URLForm(FlaskForm):
    original_link = StringField(
        'Длинная ссылка',
        validators=(
            DataRequired(message='Обязательное поле'),
            URL(message='Некорректная ссылка'),
        ),
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=(
            Length(
                max=MAX_SHORT_LINK_LENGTH,
                message="Длина поля не должна превышать 16 символов.",
            ),
            Regexp(
                SHORT_ID_VALIDATION_REGEX,
                message='Некорректная ссылка',
            ),
            Optional(),
        ),
    )
    create = SubmitField('Создать')