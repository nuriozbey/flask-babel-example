<h2 align="left" > ✨ Python-Flask-Babel-Example ✨ <img src="https://i.pinimg.com/originals/00/4b/17/004b173f6e3d6843df10114e087f30a8.gif" width="40" height="40" />  </h2> 

![GitHub issues](https://img.shields.io/github/issues/nuriozbey/flask-babel-example)   
![GitHub forks](https://img.shields.io/github/forks/nuriozbey/flask-babel-example)
![GitHub stars](https://img.shields.io/github/stars/nuriozbey/flask-babel-example)
![GitHub license](https://img.shields.io/github/license/nuriozbey/flask-babel-example)
![GitHub last commit](https://img.shields.io/github/last-commit/nuriozbey/flask-babel-example)
![GitHub repo size](https://img.shields.io/github/repo-size/nuriozbey/flask-babel-example)
![GitHub language count](https://img.shields.io/github/languages/count/nuriozbey/flask-babel-example)
![GitHub top language](https://img.shields.io/github/languages/top/nuriozbey/flask-babel-example)
![GitHub contributors](https://img.shields.io/github/contributors/nuriozbey/flask-babel-example)
![GitHub watchers](https://img.shields.io/github/watchers/nuriozbey/flask-babel-example?style=social)

Flask Application with Multi-Language Support (TR-EN-DE-FR) 

## Installation

#### Clone Repository

```bash
git clone https://github.com/nuriozbey/flask-babel-example.git
```

#### Create Virtual Environment

```bash
python -m venv venv
```

#### Activate Virtual Environment

```bash
venv\Scripts\activate
```

#### Change Directory

```bash
cd flask-babel-example
```

#### Install Requirements

```bash
pip install -r requirements.txt
```

## Usage

```bash
python .\main.py
```

#### Babel Configuration

```python
# config.py
BABEL_DEFAULT_LOCALE = 'tr'
BABEL_DEFAULT_TIMEZONE = 'Europe/Istanbul'
BABEL_TRANSLATION_DIRECTORIES = 'translations'
```

#### Translation

```python
# main.py
from flask_babel import _

@app.route('/')
def index():
    return render_template('index.html', title=_('Home'))
``` 

#### Translation File Example

```python
# translations/tr/LC_MESSAGES/messages.po
msgid "Home"
msgstr "Ana Sayfa"
```

#### Babel.cfg File example

```python
# babel.cfg
[python: **.py]
[jinja2: **/templates/**.html]
[extractors]
jinja2 = jinja2.ext.babel_extract
```

#### Extract and Compile
```bash
pybabel extract -F babel.cfg -o messages.pot .
```
 
```bash
pybabel init -i messages.pot -d translations -l tr
pybabel init -i messages.pot -d translations -l de
pybabel init -i messages.pot -d translations -l fr
pybabel init -i messages.pot -d translations -l es
```

```bash
pybabel compile -d translations
```

#### Run Application
```bash
python .\main.py
```
 


## Update Translation Files (Extract and Compile)
 
```bash
pybabel extract -F babel.cfg -o messages.pot . --no-wrap
```
 

```bash
pybabel update -i messages.pot -d translations --no-wrap
```
 

```bash
pybabel compile -d translations
```
 
#### Run Application
```bash
python .\main.py
```

## License
GNU General Public License v3.0

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

