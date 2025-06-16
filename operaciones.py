# DATOS
a = 9
b = 6

# OPERACIONES
# suma
c = a + b

# resta
d = a - b

# multiplicacion
e = a * b

# división
f = a / b

# módulo (residuo de la división)
g = a % b

# RESULTADOS
print(f'Resultado de suma es: {c}')
print(f'Resultado de resta es: {d}')
print(f'Resultado de multiplicación es: {e}')
print(f'Resultado de división es: {f}')
print(f'Resultado de porcentaje (módulo) es: {g}')

# la (f) permite mostrar el texto con la variable

# OPERADORWS LOGICOS
print('-----OPERADORES LOGICOS------')

# NOT
print('-----not------')
x = True
print(not x)# ahora es falso (False)

y = False
print(not y)#ahora es verdadero (True) 

# OR
print('-----or------')
a1=2
b1=3
# falso
print(a1 < 0  or  b1 < 0)
# verdadero
print(a1 > 0  or  b1 > 0)
# verdadero
print(a1 < 0  or  b1 > 0)
# verdadero
print(a1 > 0  or  b1 < 0)

# AND
print('-----and------')
a2=6
b2=3
# falso
print(a2 < 0  and  b2 < 0)
# verdadero
print(a2 > 0  and  b2 > 0)
# falso
print(a2 < 0  and  b2 > 0)
# falso
print(a2 > 0  and  b2 < 0)

