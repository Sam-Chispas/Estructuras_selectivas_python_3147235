'''
En un sistema de automatizacion industrial, un motor puede estatr encendido o apagado.
si la temperatura supera los 80°, el motor debe apagarse automaticamente. 
Escribir un programa que  controle el estado del motor
y lo apague si la temperatura supera los 80°.
'''
# Estado del motor
Temperatura =  int (input ("Ingresa la temperatur:"))
if Temperatura <= 80:
    print("el motor sigue funcionando")
    print("Por lo cual esta encendido")
    if Temperatura >= 70:
        print("Advertencia el motor esta llegando a su limite,")
        print("si llega a 80 se reiniciara el motor para bajar su temperatura")
else:
    print ("El motor se apago por lo cual dejo de funcioanr")
    print("el reactor se reinicio ")
    print ( F"Temperatura registrada actualmente:{Temperatura}°C")
print("fin del programa")