# variable numerica
numero=10
numero2=10.5

numero="Febrero"

# variable de texto string
nombre="Eduardo"
apellido='Ramiro'
html='''<html><p><p>'''
fecha=0
print("Hola")
print(type(nombre))
#str=string
#int=integer
#float=float
print(type(numero))
print(type(numero2))
#bool=booleam
soltero=True
calor=False
print(type(soltero))

#Variables que tienen varios Valores
#Arreglos > Listas List
edades=[10,12,40,60,'Eduardo',14.5,False,[1,2]]
#para ingresar a los valores de una lista debems indicar la Posicion que siempre empieza en 0(CERO) ademas si queremos usar valores negativos entonces la lista empezara pr la ultima psicion (-1 : la ultima posicion)
# si nosotros en la posicion  colocamos el siguiente formato : [n:m] entonces estaremos indicando que queremos ir desde la poosicion 'n' hasta <'m' NOTA: Siempre el recorrido sera de izq a der aun asi usemos posiciones negativas
print(edades[1:-1])
#JSON (JavaScript Objet Notation) I  Diccionario
curso={
    'nombre':'Backend0',
    'dificultad':'Dificil',
    'skills':[
        {
            'nombre':'Base de datos',
            'nivel':'Intermedio'
        },
        {
            'nombre':'ORM',
            'nivel':'Avanzado'
        }
    ]

}
print(curso['dificultad'])
#quiero el nivel del skill ORM
print(curso['skills'][1]['nivel'])

[PrimerMes,segundo_mes,tercer_mes,cuarto_mes,quinto_mes]=['Enero','Febrero','Marzo','Abril','Mayo']
print(PrimerMes)

personas = [{
    'nombre': 'Eduardo',
    'nacionalidad': 'peruano',
    'hobbies':[
        {
            'nombre': 'Volar drones',
            'experiencia': '2 años'
        },{
            'nombre':'Programar',
            'experiencia': '1 mes'
        }
    ]
},{
    'nombre': 'Juliana',
    'nacionalidad': 'colombiana',
    'hobbies':[
        {
            'nombre': 'Montar bici',
            'experiencia': '4 años'
        },{
            'nombre':'Bases de datos',
            'experiencia': '8 mes'
        }
    ]
}]
print(personas[0]['nacionalidad'])
print(personas[1]['hobbies'])
print(personas[0]['hobbies'][1]['experiencia'])
print(personas[1]['hobbies'][0]['nombre'], personas[1]['hobbies'][1]['nombre'])
#formas de eliminar variables o su contenido si esque  es una lista ,dicionario u otro
del personas