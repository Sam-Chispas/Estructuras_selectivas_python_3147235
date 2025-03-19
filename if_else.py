'''
if else:
Determina dos caminos de ejecución, basados en la evaluación de una condicional
Sintaxis:
if condicional:
Intruccion1
Intruccion2
else:
Intruccion3
Intruccion4
'''
#ejemplo:
#Elabore un programa en python
#Qué determine si una persona
#Es mayor o menor de edad
#Y por tanto, habilitada para
#Votar
edad = 1214
documento = True
if edad >= 18 and  documento==True:
    print("usted tiene documento")
    print("Usted es mayor de edad")
    print("Puede votar")
else:
    print ("Usted no tiene documento")
    print("Por lo tanto eres menor de edad")
    print("No puedes votar")
print("fin del programa")
