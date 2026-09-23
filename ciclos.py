#Explicacion: Ciclo For Repite cantidades de veces.

#Mostrar mensaje "Hola mundo 10 veces"

mensaje =input("Que mensaje quieres mostrar: ")
cantidad = int(input("Cuantas veces quiere repetir el mensaje: "))

for i in range(cantidad):
    print(f"{i} : {mensaje}")


print("="*30)
# Ejercicio 1: Mostrar la tabla de multiplicar de un número

numero = int(input("Ingrese un número para ver su tabla de multiplicar:  "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


print("="*30)
# Ejercicio 2: Sumar los primeros n números naturales

n= int(input("Ingrese un número entero positivo: "))

suma = 0
for i in range(1, n + 1):
    suma = suma + i 


print("="*30)
#Ciclo for que se repita 3 veces

numero_secreto= 8
intentos = 3

for i in range(intentos):
    numero = int(input("Adivina el número secreto: "))

    if numero == numero_secreto:
        print("¡Felicidades! Adivinaste el número. ") 
        break
    
    else:
        intentos_restantes =intentos - (i+1)
        print(f"Te quedan {intentos_restantes} intentos. ")

        if intentos_restantes == 0 :
            print(f"El número era {numero_secreto}")


print("="*30)
#Ciclo for que se repita 3 veces V2
import random

numero_secreto= random.randint(1, 10)
intentos = 3

for i in range(intentos):
    numero = int(input("Adivina el número ENTRE 1 Y 10 "))

    if numero == numero_secreto:
        print("¡Felicidades! Adivinaste el número. ") 
        break
    
    else:
        intentos_restantes =intentos - (i+1)
        print(f"Te quedan {intentos_restantes} intentos. ")

        if intentos_restantes == 0 :
            print(f"El número era {numero_secreto}")

        #condicion si el numero es mayor o menor al numero secreto

        if numero > numero_secreto: 
            print("Pista: Muy Alto.")

        if numero < numero_secreto:
            print("Pista: Muy bajo")


print("="*30)
# Ejercicio 3: Contar cuántos números pares hay entre 1 y n

n = int(input("Ingrese un número entero positivo: "))

contador = 0
numero   = 1
while numero <= n:
    if numero % 2 == 0:
        contador = contador + 1
    numero = numero + 1

print(f"Hay {contador} números pares entre 1 y {n}")


print("="*30)
# Ejercicio 4: Solicitar una contraseña hasta que sea correcta

clave_correcta  = "python2026"
clave_ingresada = input("Ingrese la contraseña: ")

while clave_ingresada != clave_correcta:
    print("Contraseña incorrecta, intente de nuevo")
    clave_ingresada = input("Ingrese la contraseña: ")

print("Contraseña correcta, acceso concedido")


print("="*30)
# Ejercicio 5: Calcular el factorial de un número

n = int(input("Ingrese un número entero no negativo: "))

factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i

print(f"El factorial de {n} es: {factorial}")

