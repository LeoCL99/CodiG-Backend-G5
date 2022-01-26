from logging import debug
from flask import Flask
# en python tenemos variables que son de uso propio de pytho no podemos modificar ni alterar
# __name__> es variable sirve para indicar si estamos en el archivo principal del proyecto
app = Flask(__name__)
# el decorador sirve para usar el metodo de una clase pero implementando en una funcion


@app.route('/')
def inicio():
    return 'Bienvenido a mi API'


@app.route('/bienvenido')
def bienvenido():
    return 'Te doy la bienvenida a mi API'


@app.route('/bienvenido/home')
def bienvenido_home():
    # solamente podemos retornar los siguientes tipos de datos:String, tupla y diccionarios
    return 'Te doy la bienvenida a mi API home'


if __name__ == '__main__':
    # para que cada vez que nosotros hagamos algun cambio en cualquier archivo del proyecto y se  reinicie autmaticamente
    # entonces deberemos indicar el parametro debug con el valor de True(cuyo valor por defecto es False)
    app.run(debug=True)
