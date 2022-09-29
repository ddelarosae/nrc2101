# Importar "render_template"
from flask import Flask, render_template
# Crear la instancia de Flask
app = Flask(__name__)
# Definir el route
@app.route('/')
# Un segundo route con el nombre del parámetro
@app.route('/<string:nombre>')
def render(nombre=None): # Inicializa "nombre"
	# Retornar plantilla "index.html y pasar parámetro a  el método render_template
    return render_template("ej5.html", dato=nombre)
