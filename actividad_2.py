'''
Una universidad ofrece un descuento a los estudiantes que dependen del  estrato y la
edad. Si el estrato es 1 y su edad es menor a 18 el descuento será del 20% sobre el valor
de la matrícula. Si el estrato es 1 y alumnos tiene 18 o mas años , el descuento sera
del 10%, y si el estrato es 2 y la edad es 18 años o mas, el descuento sera del 5%.
'''

# Procedimiento
estrato = int(input("Digite un estrato: "))
edad = int (input ("Digite una edad:"))
valor_matricula= int (input ("Digite la matricula:"))
# Calcular descuento
if estrato == 1 and edad < 18:
    descuento = valor_matricula * 0.20
elif estrato == 1 and edad >= 18:
    descuento = valor_matricula * 0.10
elif estrato == 2 and edad >= 18:
    descuento = valor_matricula * 0.05
else:
    descuento = 0  # No hay descuento

# Calcular matrícula con descuento
valor_matricula_descuento = valor_matricula - descuento

# Mostrar resultados
print(f'El valor de la matrícula es: ${valor_matricula}')
print(f'El descuento es: ${descuento}')
print(f'El valor de la matrícula con descuento es: ${valor_matricula_descuento}')