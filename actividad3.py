'''
Actividad 3:
Elabore un programa que permita calcular el salario neto de un empleado, despues descontar los 
descuentos por conceptos de:  
Salud, pensón , ARL
1. El progama debe solicitar el tipo de empleado:
a- contrato a termino indefinido
b- Contrato por prestacion de servicio
c- Contrato de aprendizajo
d- Contrato por jornada  (Freelance)
=> Para el caso de jornada:
Se debe solicitar numero de horas trabajadas el valor a pagar por hora
El total del salario se calcula  de multiplicar el numero de horas por el valor 
a pagar por horas
'''
#Inicializar variables, dar valor inicial de una variable asi no se utilice en ese momento
contrato = input ("Ingrese el tipo de contrato:")
salario_neto= 0

if contrato == "a":
    print ("Eligio: contrato a termino indefinido")
elif contrato =="b":
    print ("Eligio contrato  por prestación de servicio")
elif contrato =="c":
    print ("Eligio:contrato de aprendizaje")
    salario_minimo= int(input("Ingrese el valor del salario minimo"))
    salario_neto=  salario_minimo-(salario_minimo*0.25)
    
elif contrato == "d":
    print ("Eligio: Contrato por jornada")
    valor_neto =0
    numero_horas = int(input("Ingrese su numero de horas:"))
    valor_hora =int(input("Ingrese el valor a pagar por hora:"))
    salario_neto =  numero_horas* valor_neto
    

else:
    print ("No hay ningun tipo de contraro, colcoa uno si es a,b,c o d ")

print ("El salario neto es:",salario_neto)
print ("No colocaste un salario neto")
print ("Fin de programa")

