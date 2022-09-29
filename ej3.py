from flask import Flask
app = Flask(__name__)
@app.route('/hola/')
@app.route('/hola/<string:nombre>')
@app.route('/hola/<string:nombre>/<int:edad>')
def hola(nombre=None,edad=None):
    if nombre and edad:
        return "Hola, {} tienes {} años".format(nombre,edad)
    elif nombre:
        return "Hola, {}".format(nombre)
    else:
        return "Hola mundo"