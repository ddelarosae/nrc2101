from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('sesion.html')
@app.route('/mintic')
def mintic():
    return "Pagina del MINTIC"
@app.route('/daniel')
def daniel():
    return "Pagina del formador Daniel"