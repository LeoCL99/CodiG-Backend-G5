

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
        return self.__velocidad

    def get_velocidad(self):
        return self.__velocidad


class VehiculoVolador(Vehiculo):
    def __init__(self, color, modelo, traccion, vuela=False):
        super().__init__(color, modelo, traccion)
        self.__vuela = vuela

    def volar(self):
        self.__vuela = True

    def aterrizar(self):
        self.__vuela = False

    def estado(self):
        estado_volando = 'esta volando' if self.__vuela else 'esta aterrizando'
        return 'el vehiculo es de color:{} moelo:{} traccion:{} velocidad:{} y {}'.format(self.color, self.modelo, self.traccion, self.get_velocidad(), estado_volando)


class VehiculoOffRoad(VehiculoVolador):
    def __init__(self, color, modelo, traccion, vuela=False, sumergido=False):
        super().__init__(color, modelo, traccion, vuela)


obj_vehiculo = Vehiculo('verde', 'rx5', '4x4')
obj_vehiculo_volador = VehiculoVolador('blanco', 'xyz', '4x2')
# obj_vehiculo_volador.volar()
obj_vehiculo_volador.acelerar()
# print(obj_vehiculo_volador.vuela)#debe lanzar un error que no existe

print(obj_vehiculo_volador.color)


obj_vehiculo_offroad = VehiculoOffRoad('azul', 'asda', '4x2')
obj_vehiculo_offroad.acelerar()
obj_vehiculo_offroad.desacelerar()
obj_vehiculo_offroad.volar()
# primero que el atributo vuela sea privado y luego tener un estado llamado estado
# en el cual se indique cual es el estado del vehiculo,que me diga su color,
# modelo,traccion,velocidad y si esta volando o si esta aterrizando
print(obj_vehiculo_volador.estado())
# isintance()>devolvera True si es que la instancia es de la clase
# si esa instancia es de una class
print(isinstance(obj_vehiculo_offroad, VehiculoOffRoad))

# issubclass()
print(issubclass(VehiculoOffRoad, Vehiculo))
