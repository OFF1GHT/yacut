from flask import render_template, flash, redirect, abort
from sqlalchemy.exc import IntegrityError

from . import app
from .forms import URLForm
from .url_shortener import URL


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        try:
            short_url = URL(
                form.original_link.data, form.custom_id.data
            ).get_short_link()
        except IntegrityError:
            flash(
                'Предложенный вариант короткой ссылки уже существует.',
                'already_exists',
            )
            return render_template('index.html', form=form)
        flash(short_url, 'new_url')
        return render_template('index.html', form=form)
    return render_template('index.html', form=form)


@app.route('/<id>')
def redirect_view(id):
    url_handler = URL()
    original_url_object = url_handler.get_url(id)
    if not original_url_object:
        abort(404)
    return redirect(original_url_object.original)
