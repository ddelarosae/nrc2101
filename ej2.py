from flask import Flask
app = Flask(__name__)
@app.route('/productos/<int:id>')
def mostrar_producto(id):
    return "id {} del artículo".format(id)
@app.route('/articulos/<string:id>')
def mostrar_articulos(id):
    return "Mostrar el artículo con id: "+id
