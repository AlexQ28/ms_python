# name = input('Please enter your name: ')
# print(name)

# print('Hello World')
# print()
# print('Did you see that blank line?')
# print('Blank line \nin the middle of string')

#print('Hello \nworld')

# nombre = input("¿Cual es tu nombre?")
# mensaje = "Hola " + nombre
#print(mensaje)

#Numeros
# a = 45
# b = 0.43
# c = 4 + 6j
# print(type(a))
# print(type(b))
# print(type(c))

#Cadenas
# msj = "Hola a todos"
# mjs2 = 'Hola Mundo'
# parrafo = """Esto es un texto de varias lineas """
# print(msj)
# print(mjs2)
# print(parrafo)
# print(type(parrafo))

#Booleano
# verd = True
# falso = False
# print(type(verd))
# print(type(False))

#Expresiones Artiméticas

"""
Suma              ->(+)
Resta             ->(-)
Producto          ->(*)
División          ->(/)
División Entera   ->(//)
Exponenciación    ->(**)
Resto o Modulo    ->(%)
"""
# a = 92
# b = 13

# suma = a + b 
# print(suma)

# resta = a - b
# print(resta)

# producto = a * b
# print(producto)

# division_exacta = a/b
# print(division_exacta)

# division_entera = a//b 
# print(division_entera)

# residuo = a % b
# print(residuo)

"""
OPERADORES DE ASIGNACIONES
"""
# x = 10
# x += 4 # x = x + 4
# print (x)
# x -= 7
# print(x)
# x *= 3
# print(x)

# x **=2
# print(x)

# x /= 5
# print(x)

# x //= 6
# print(x)

# x %= 3
# print(x)

"""
Reglas de Prioridad
=====================
*PEMDAS"
P Parentesis primero
E Exponentes (potencias y raices cuadradas, etc.)
MD Multiplicacion y Division (de izquierda a derecha)
AS Adición y Sustracción (de izquierda a derecha)
"""
# m = 10
# n = 14
# q = 3
# r = 6

# z =  (m*(n-q**3 )-m)+r*m-5
# #z =  (m*(n- 27 )-m)+r*m-5
# #z =  (m*(-13   )-m)+r*m-5
# #z =  (    -130  -m)+r*m-5
# #z =       -140     +60 -5
# #z =            -85
# print(z)

#MANIPULACION DE CADENAS DE TEXTO
# titulo = r"Estoy aprendiendo a programar en Python 2020 :D\n\n"
# subtitulo =r"\t\tAhora soy un programador"

# contenido = titulo + subtitulo
# print(contenido)

# #MULTIPLICAR CADENAS
# word = "123"
# producto = word*4
# print(producto)

# #INDICES DE UNA CADENA DE TEXTO
# #Indices
# word = "Hola Mundo"
"""
indice -> Valor
word[0] -> H
word[1] -> o
word[2] -> l
word[3] -> a
word[4] -> M
....
word[9] -> o
"""
# print(word[3])

# word = "Hola Mundo!"
# print(word[4:8])

# #indice negativo
# print(word[-8:-4])
# print(word[-4:-8]) #Manda vacio 

# print(word[-8:])
# print(word[:-8])
# print(word[:4])

# print(word[:])

# #*****OPERADORES LOGICOS O CONDICIONALES*****
# #Operador and
# #la expresion es verdadera, si a y b son verdaderos 
# a = False
# b = False

# x = a and b # es lo mismo decir b and a 
# print (x)

# #Operador or 
# #la expresion es verdadera, si al menos una de las partes
# #(a o b) es verdadera

# x = a or b #es lo mismo decir b or a
# print(x)

# #Operador not
# x = not a
# print(x)

# #Expresion Booleana
# a = True
# b = True
# c = False 

# #orden de precedencia
# """
# not
# and
# or
# """
# m = a and not b or c 
# #m = a and False or c
# #m =       False or c
# #m =         False
# print(m)

#******OPERADORES RELACIONALES*******
# print("------Operadores relacionales-------")
# x = 10 
# y = 14
# z = 4

# print(x == y)
# print(y == x+z)
# print(y <= x)
# print(z > y)

"""
Orden de Precedencia
==,<,>,>=,<=  Operadores Relacionales son de Mayor relevancia
not    Operadores Logicos o Condicionales 
and
or
"""

x = 11 
print("expr1 = not x > 10")
expr1 = not x > 10
print(expr1)

#cualquier valor diferente de cero es considerado True
#False -> 0
print("expr2 = (not x) > 10")
expr2 = (not x) > 10
print(expr2)

x = 10
y = 14
z = 4

print("expr3 = not x > 10 or (y == z and x <= y)")
expr3 = not x > 10 or (y == z and x <= y)
#expr3 = not x > 10 or (False and True)
#expr3 = not x > 10 or False
#expr3 = not False or False 
#expr3 = True
print(expr3)



















































#El parentesis interno es el primero a evaluar



















































































