'''
if aninados:
if dentro de otros if
syntax:
    if condicion1:
    print ("mensaje")
    
else:
    print ("mensaje")
confundir con elif (if en cascadas)

'''
#Ejemplo 1:
#Modifique el ejercicio de la edad para las siguientes condiciones

#1.) si es mayor de 18 años pero no tiene docuemntos, no puede votar 

#De lo contrario si puede votar 

#2.) Si es menor de 18 años, no puede votar

#Utilice las estructuras de if anidados 


edad = int(input("ingresa su edad:"))
if edad >= 18:
    documento = input ("Tiene document, (si / no)")
    if documento == "si": 
        print("puede votar")
    else:
        print ("No puede votar")
else:
    print ("No puede votar")