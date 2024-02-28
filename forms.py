from wtforms import Form
from wtforms import StringField,TelField, IntegerField
from flask_wtf import FlaskForm
from wtforms import EmailField

from wtforms import validators
class UserForm(Form):
  nombre=StringField("nombre",[
    validators.DataRequired("El campo es requerido"),
    validators.length(min=0,max=10, message="Ingresa nombre valido")
  ])
  apaterno=StringField("apaterno",[
    validators.DataRequired("El campo es requerido"),
    validators.length(min=0,max=10, message="Ingresa apellido valido")
  ])
  amaterno=StringField("amaterno",[
    validators.DataRequired("El campo es requerido"),
    validators.length(min=0,max=10, message="Ingresa apellido valido")
  ])
  email=EmailField("email",[validators.Email(message="Ingresa un correo valido")])
  edad=IntegerField("edad",[validators.DataRequired("El campo es requerido")])
  
class UserForm2(Form):
  id = IntegerField('id', [validators.number_range(min=1, max=20, message='Valor no valido')])
  nombre = StringField('nombre', validators=[
    validators.DataRequired(message='El nombre es requerido'),
    validators.length(min=4, max=20, message='Requiere min=4, max=10')
  ])
  apaterno = StringField('apaterno', validators=[
    validators.DataRequired(message='El apellido es requerido')
  ])
  email = EmailField('correo', validators=[ 
    validators.Email(message='El email es requerido')
  ])