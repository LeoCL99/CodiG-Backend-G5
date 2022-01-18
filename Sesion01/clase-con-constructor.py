import re


class Vehiculo:
    """"Clase que sirve para el uso e los vehiculos"""

    def __init__(self, color, modelo, traccion):
        self.color = color
        self.modelo = modelo
        self.traccion = traccion
        # encapsulado el atributo velocidad para que no pueda ser accedido afuera de la clase

        self.__velocidad = 0

    def acelerar(self):
        '''Metodo que acelera el vehiculo de 20 en 20'''
        self.__velocidad += 20
        return 'La velocidad actual es: {} km/h'.format(self.__velocidad)

    def desacelerar(self):
        '''Metodo que desacelara el vehiculo en 20km/h'''
        self.__velocidad -= 20
        self.__prueba()
        return self.__velocidad

    def __prueba(self):
        '''Metodo privado de la clase que solo puee ser accedido debtri de la misma'''
        print('Esto no deberia de pasar')


Vehiculo1 = Vehiculo('Azul', 'x3', '4x2')
print(Vehiculo1.acelerar())
print(Vehiculo1.acelerar())
print(Vehiculo1.acelerar())
print(Vehiculo1.desacelerar())
