import os
from flask import Flask, redirect, render_template, request, send_from_directory, session, url_for
from flask_babel import Babel, gettext, _get_current_context
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
extra_files = ['./translations/tr/LC_MESSAGES/messages.mo',
               './translations/de/LC_MESSAGES/messages.mo',
               './translations/fr/LC_MESSAGES/messages.mo',
               './translations/es/LC_MESSAGES/messages.mo']

app.config['LANGUAGES'] = {
    'en': 'English',
    'tr': 'Turkish',
    'de': 'German',
    'fr': 'French',
    'es': 'Spanish'
}


def get_locale():
    # return 'en'
    language = session.get('language')
    if language is None:
        language = request.accept_languages.best_match(
            app.config['LANGUAGES'].keys())
        session['language'] = language
    if request.method == 'POST':
        if "language" in request.form:
            language = request.form['language']
            session['language'] = language
    return language


babel = Babel(app, locale_selector=get_locale)


@app.route('/setlocale', methods=['GET', 'POST'])
def set_locale():
    if request.method == 'POST':
        if "language" in request.form:
            # print(locale)
            session['language'] = request.form['language']
            session['locale'] = request.form['language']
            # print(session['locale'])
            # app.config['BABEL_DEFAULT_LOCALE'] = locale
            return redirect(url_for('index'))
        # session['locale'] = request.form['language']
    elif request.method == 'GET':
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            session['locale'] = locale
            session['language'] = locale
    return redirect(request.referrer)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/media'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def index():
    return render_template('index.html', language=app.config['LANGUAGES'][session['language']])


### swagger part ###
SWAGGER_URL = '/docs'
URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    URL,
    config={
        'app_name': "Python-Flask-Babel-Example-Swagger"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger part ###
