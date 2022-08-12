from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

from models.log.Controllers import User



class ModelUser(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    fullname = db.Column(db.String(100))
    cedula = db.Column(db.Integer)
    nacimiento = db.Column(db.Date)
    email = db.Column(db.String(50),unique=True)
    tipo_usuario = db.Column(db.String(6),default = "user")


    