nombre = input("Ingrese su Nombre:")

edad = int(input("Ingrese su edad:"))

hora = int(input("Ingrese la hora:"))

if edad>=18 and hora >=6 :
    print("No estas obligado a hacer nada porque eres mayor de edad")
elif edad>=18 and hora <=6:
     print("No estas obligado a hacer nada porque eres mayor de edad")
    
elif edad<18 and hora >=6:
     print("Tienes que irte a dormir")
else:
    print("Tienes que hacer la tarea")