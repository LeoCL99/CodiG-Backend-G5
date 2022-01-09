from flask import Flask
#en python tenemos variables que son de uso propio de pytho no podemos modificar ni alterar
#__name__> es variable sirve para indicar si estamos en el archivo principal del proyecto
app=Flask(__name__)
#el decorador sirve para usar el metodo de una clase pero implementando en una funcion
@app.route('/')
def inicio():
    return 'Bienvenido a mi API'
app.run()