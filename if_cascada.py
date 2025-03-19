'''
if cascada:
Es una estructura selectiva
compuesta por multiples
condicionales,seguidos
unos de otros

sintaxis:
if condicional_1:
    intruccion1
    intruccion2
    
elif condicional_2:
    intruccion3
    instrccion4
    
elif condicional_3:
    instruccion5
    instruccion6

NOTA: cada condicional
es MUTUAMENTE EXCLUYENTE
'''
#EJEMPLO:
#ELABORAR UN PROGRAMA PEQUEÑO DE UN TRADUCTOR
#LEER UNA FRUTA EN ESPAÑOL
#Y DEBE MOSTRARLO ESA FRUTA EN INGLES
Fruta_es = input ("Ingresar una fruta:")
if Fruta_es =="manzana" or  Fruta_es == "manzana":
    print("apple")
elif Fruta_es =="Fresa" or Fruta_es =="Fresa":
    print("strawberry")
elif Fruta_es == "platano" or Fruta_es == "platano ":
    print("banana")
elif Fruta_es == "naranja" or Fruta_es == "naranja":
    print("orange")
elif Fruta_es == "Uva" or Fruta_es == "Uva":
    print ("grape")
    print ("fin del progrma")
    
#por defecto
else:
    print("no se reconoce la fruta")
