from flask import Flask, render_template, request, flash
import utils
import yagmail
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('sesion.html')
@app.route('/login')
def login():
    return render_template('ejPractico9_login.html')
@app.route('/register',methods=('GET','POST'))
def register():
    try:
        if request.method == 'POST':
            username = request.form['usuario']
            password = request.form['pass']
            email = request.form['correo']
            if not utils.isUsernameValid(username):
                error="El usuario debe ser alfanumerico"
                flash(error)
                return render_template('error.html')
            if not utils.isPasswordValid(password):
                error="La contraseña debe tener al menos 8 caracteres"
                flash(error)
                return render_template('error.html')
            if not utils.isEmailValid(email):
                error="El email debe ser alfanumerico"
                flash(error)
                return render_template('error.html')
            yag=yagmail.SMTP('danieldelarosa.ruta1@utp.edu.co','Qn$w+?3x.ACg')
            yag.send(to=email, subject='Cuenta creada', contents='Se ha creado su usuario')
            flash('Verifique su correo electronico')
            return render_template('ejPractico9_login.html')
        return render_template('sesion.html')
    except:
        return render_template('sesion.html')        