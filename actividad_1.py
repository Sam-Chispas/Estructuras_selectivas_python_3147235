'''
En un sistema de automatizacion industrial, un motor puede estatr encendido o apagado.
si la temp2ratura supera los 80°, el motor debe apagarse automatizamente. 
escribir un programa que  controle el estado del motor
y lo apague si la temperatura supera los 80°.
'''
# Estado del motor
Temperatura = 89
if Temperatura <= 80:
    print("el motor sigue funcionando")
    print("Por lo cual esta encendido")
else:
    print ("El motor se apago por lo cual dejo de funcioanr")
    print("el reactor se apago")
print("fin del programa")