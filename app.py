from flask import Flask,request,make_response,redirect,render_template,flash,url_for
from Forms.forms import FormLogin, FormSignin, FormReserva
""" from settings.config import config """
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

""" #Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User """


app=Flask(__name__)

app.config['SECRET_KEY'] = '0f1bf7b724784b746e76e834'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logindb.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

Login_manager = LoginManager(app)
Login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    fullname = db.Column(db.String(100))
    cedula = db.Column(db.Integer)
    nacimiento = db.Column(db.Date)
    email = db.Column(db.String(50),unique=True)
    tipo_usuario = db.Column(db.String(6),default = "user")

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String(50), unique=True)
    available = db.Column(db.Boolean, default = True)
    score = db.Column(db.Integer)


@Login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def inicio():
    return render_template("index.html")

@app.route("/reserva", methods=["GET","POST"])
def reserva():   
    form_login=FormLogin()
    form_reserva=FormReserva()
    if login_user != None:        
        if form_login.validate_on_submit():
            user = User.query.filter_by(username=form_login.username.data).first()
            if check_password_hash(user.password, form_login.password.data):
                login_user(user, remember=form_login.remember.data)
                return render_template("logged.html", name=current_user.fullname)
            else:
                return '<h1>"Usuario o Contraseña invalida" </h1>'
    else:
        return render_template("logged.html", name=current_user.fullname)

    return render_template("login.html", form=form_login)

@app.route('/signin', methods=["GET","POST"])
def signin():
    form_signin=FormSignin()
    form_reserva=FormReserva()

    if form_signin.validate_on_submit():
        hashed_password = generate_password_hash(form_signin.password.data, method='sha256')
        new_user = User(username=form_signin.username.data, password=hashed_password, fullname=form_signin.fullname.data, cedula=form_signin.cedula.data, nacimiento=form_signin.nacimiento.data, email=form_signin.email.data)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>Se a creado un nuevo usuario</h1>'


    return render_template("signin.html", form=form_signin)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('reserva'))

@app.route("/prueba")

def prueba():
    form=FormSignin()
    return render_template("reserva_prueba.html", form=form)


if __name__ == "__main__":
    """ app.config.from_object(config["development"]) """
    app.run(host='0.0.0.0', debug=True)