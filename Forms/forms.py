from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired, Length

class FormLogin(FlaskForm):
    username=StringField("Usuario",validators=[DataRequired(message="Ingresa tu usuario")])
    password= PasswordField("Contraseña",validators=[DataRequired(message="Ingresa tu contraseña"), Length(min=8, max=80)])
    remember= BooleanField("Recordar usuario")
    submit= SubmitField("Iniciar Sesion")

class FormSignin(FlaskForm):
    fullname=StringField("Nombre",validators=[DataRequired(message="ingresa tu nombre")])
    cedula=IntegerField("Cedula",validators=[DataRequired(message="ingresa tu numero de cedula")])
    nacimiento=DateField("Fecha de Nacimiento", validators=[DataRequired(message="ingresa tu fecha de nacimineto")])
    email=StringField("Correo",validators=[DataRequired(message="ingresa tu Correo electronico")])
    username=StringField("Usuario",validators=[DataRequired(message="ingresa un usuario")])
    password=PasswordField("Contraseña",validators=[DataRequired(message="ingresa una contraseña"), Length(min=8,message="La contraseña debe tener minimo 8 caracteres")])
    submit=SubmitField("Registrate")

class FormReserva():
    arrival=DateField("Fecha de llegada",validators=[DataRequired(message="ingresa la fecha de llegada")])
    departure=DateField("Fecha de salida",validators=[DataRequired(message="ingresa la fecha de salida")])
    submit= SubmitField("Buscar habitaciones disponibles")

