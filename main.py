from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g
from config import DevelopmentConfig
import forms

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.errorhandler(404)
def page_not_found(e):
 return render_template("404.html"),404

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
  alumno_clase=forms.UserForm(request.form)
  nom=""
  apa=""
  ama=""
  edad=""
  email=""
  if request.method=="POST" and alumno_clase.validate():
    nom=alumno_clase.nombre.data
    apa=alumno_clase.apaterno.data
    ama=alumno_clase.amaterno.data
    edad=alumno_clase.edad.data
    email=alumno_clase.email.data
    print("Nombre: {}".format(nom))
    print("Apaterno: {}".format(apa))
    print("Amaterno: {}".format(ama))
    print("Edad: {}".format(edad))
    print("Email: {}".format(email))
    
    mensaje="Bienvenido {}".format(nom)
    flash(mensaje)
  return render_template("alumnos.html", form=alumno_clase, nom=nom, apa=apa, ama=ama, edad=edad, email=email)

if __name__=="__main__":
  csrf.init_app(app)
  app.run()
  