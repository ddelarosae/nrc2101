from flask import Flask, render_template,flash, redirect,url_for
from forms import FormInicio
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', titulo='Inicio')
@app.route('/login',methods=['GET','POST'])
def login():
    form = FormInicio()
    if(form.validate_on_submit()):
        flash('Inicio de sesión solicitado por el usuario {}, recordar={}'.format(form.usuario.data,form.recordar.data))
        return redirect(url_for('gracias'))
    return render_template('iniciar_sesion.html', titulo='Iniciar Sesión', form=form)

@app.route('/gracias')
def gracias():
    return render_template('gracias.html')

