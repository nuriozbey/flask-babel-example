# flask-babel-example
Flask Application with Multi-Language Support (TR-EN-DE-FR) 

## first
##

```javascript
pybabel extract -F babel.cfg -o messages.pot .
```
 
```javascript
pybabel init -i messages.pot -d translations -l tr
pybabel init -i messages.pot -d translations -l de
pybabel init -i messages.pot -d translations -l fr
pybabel init -i messages.pot -d translations -l es
```

```javascript
pybabel compile -d translations
```

```javascript
python .\main.py
```
 


### update

 
```javascript
pybabel extract -F babel.cfg -o messages.pot . --no-wrap
```
 

```javascript
pybabel update -i messages.pot -d translations --no-wrap
```
 

```javascript
pybabel compile -d translations
```
 

```javascript
python .\main.py
```