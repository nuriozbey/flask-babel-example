import os
from flask import Flask, redirect, render_template, request, send_from_directory, session, url_for
from flask_babel import Babel, gettext, _get_current_context
from flask_swagger_ui import get_swaggerui_blueprint

# initialize the Flask application
app = Flask(__name__)
app.secret_key = 'secret_key'

# set the default language to English and the default timezone to Istanbul
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'Europe/Istanbul'

# set the path to the translation files
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'

# define a dictionary of available languages
app.config['LANGUAGES'] = {
    'en': 'English',
    'tr': 'Turkish',
    'de': 'German',
    'fr': 'French',
    'es': 'Spanish'
}

# define a function to determine the user's preferred language
def get_locale():
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


# initialize the Babel extension with the Flask application and the locale selector function
babel = Babel(app, locale_selector=get_locale)

# define a route to set the user's preferred language
@app.route('/setlocale', methods=['GET', 'POST'])
def set_locale():
    if request.method == 'POST':
        if "language" in request.form:
            session['language'] = request.form['language']
            session['locale'] = request.form['language']
            return redirect(url_for('index'))
    elif request.method == 'GET':
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            session['locale'] = locale
            session['language'] = locale
    return redirect(request.referrer)

# define a route for the favicon.ico file
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/media'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


# define a route for the home page
@app.route('/')
def index():
    return render_template('index.html', language=app.config['LANGUAGES'][session['language']])

########################
### Swagger UI Usage ###
########################
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
