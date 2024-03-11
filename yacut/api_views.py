from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
from http import HTTPStatus

from . import app
from .error_handlers import (
    InvalidAPIUsage,
    MissingRequiredParameterError,
    ValidationError,
)
from .services import URL


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    try:
        short_link = URL(
            data.get('url'), data.get('custom_id')
        ).create_short_link()
    except IntegrityError:
        raise InvalidAPIUsage(
            'Предложенный вариант короткой ссылки уже существует.'
        )
    except ValidationError:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    except MissingRequiredParameterError:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')

    return jsonify({'url': data.get('url'), 'short_link': short_link}), 201


@app.route('/api/id/<id>/', methods=['GET'])
def get_url(id):
    original_url_object = URL().get_url(id)

    if not original_url_object:
        raise InvalidAPIUsage('Указанный id не найден', 404)

    return jsonify({'url': original_url_object.original}), HTTPStatus.OK