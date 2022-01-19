class Electrodomestico:
    def __init__(self):
        self.__nombre = ''
        self.__precio = 0.0
        self.__color = ''
# getter>sirve para devolver el contennido de un atributo privado
# setter>sirve para asignar el contenido de un atributo privado que no sea en el constructor
# deletter>sirve para eliminar un atributo privado

    def __getNombre(self):
        return self.__nombre

    def __setNombre(self, nombre):
        self.__nombre = nombre

    def __deleteNombre(self):
        del self.__nombre

    nombre = property(__getNombre, __setNombre, __deleteNombre)


microondas = Electrodomestico()
microondas.nombre = 'Microondas'
print(microondas.nombre)
