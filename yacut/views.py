from flask import render_template, flash, redirect, abort
from sqlalchemy.exc import IntegrityError

from . import app
from .forms import URLForm
from .services import URL


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        try:
            short_url = URL(
                form.original_link.data, form.custom_id.data
            ).create_short_link()
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
    original_url_object = URL().get_url(id)
    if not original_url_object:
        abort(404)
    return redirect(original_url_object.original)
