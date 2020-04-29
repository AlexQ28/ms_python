# a = input() #Funcion input nos da un valor de tipo cadena
# a = int(a)   #Funcion int nos permite convertir la cadena como entero
# es_par = a%2 == 0

# if es_par:
#     print("Es Par")
#     print("Hola")
#     print(es_par)

# print("FIN")

# a = input("Valor de a:")
# a = int(a)

# b = input("Valor de b:")
# b = int(b)

# o = input("Operadores:(+) (-) (/) ")

# if o == "+":
#     R = a+b
# elif o == "-":
#     R = a-b
# elif o == "/":
#     R = a/b
# else:
#     R = "Operador no valido"

# print(R)    

"""
IF ANIDADO
"""
# a = input("a =")
# a = int(a)

# b = input("b =")
# b = int(b)

# c = input("c =")
# c = int(c)

# if a>b:
#     if a>c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b>c:
#         print(b)
#     else:
#         print(c)

# print("FIN") 

"""

De calificación numérica a calificación alfabética
Se tiene el siguiente sistema de calificación, donde la calificación:
* Mayor o igual a 19 es A
* Menor a 19 y mayor o igual a 17 es B
* Menor a 17 y mayor o igual a 15 es C
* Menor a 15 y mayor o igual a 13 es D
* Menor a 13 es F
Se le pide a usted escribir en Python un programa que permita convertir 
una nota numérica en una calificación alfabética teniendo en cuenta lo anterior.
"""

# a = input("Ingresa tu calificacion:")
# a = int(a)
# if a >= 19: 
#     mensaje = "Tu calificacion es: A" 
#     print(mensaje)
# elif a < 19 and a >= 17:
#     mensaje = "Tu calificacion es: B" 
#     print(mensaje) 
# elif a < 17 and a >= 15:
#     mensaje = "Tu calificacion es: C" 
#     print(mensaje) 
# elif a < 15 and a >= 13:
#     mensaje = "Tu calificacion es: D" 
#     print(mensaje) 
# else:
#     a < 13
#     mensaje = "Tu calificacion es: F" 
#     print(mensaje)

"""
Calculando la nómina de un trabajador
El pago de un trabajador se calcula teniendo en cuenta los siguientes criterios:
* Sueldo básico: 1000
* El pago por hora extra es de S/ 25.00 por hora
* Si la cantidad de horas extras supera las 15 horas, entonces el pago por hora extra adicional es de S/ 30.00 por hora
* Si su sueldo supera los 1500, se le deducirán impuestos por 8% del monto total.

Se le pide escribir un programa en python que le permita calcular el sueldo final,
teniendo como entrada la cantidad de horas extras.

"""
# sueldo_basico = float(input("Ingresa tu sueldo base: "))
# sueldo_basico = float(int(sueldo_basico))

# horas_extra = input("Ingresa tus horas extras: ")
# horas_extra = int(horas_extra)

# if horas_extra >= 15:
#     pago = (horas_extra * 30) + sueldo_basico
# else:
#     horas_extra <= 15
#     pago = (horas_extra * 25) + sueldo_basico
# if pago >= 1500:
#    pago = (pago * 0.08) - pago
#    print(pago)
# else:
#     pago <= 1500
#     print(pago)
    

























    