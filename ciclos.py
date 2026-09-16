#Explicacion: Ciclo For Repite cantidades de veces.

#Mostrar mensaje "Hola mundo 10 veces"

mensaje =input("Que mensaje quieres mostrar: ")
cantidad = int(input("Cuantas veces quiere repetir el mensaje: "))

for i in range(cantidad):
    print(f"{i} : {mensaje}")


# Ejercicio 1: Mostrar la tabla de multiplicar de un número

numero = int(input("Ingrese un número para ver su tabla de multiplicar:  "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


# Ejercicio 2: Sumar los primeros n números naturales

n= int(input("Ingrese un número entero positivo: "))

suma = 0
for i in range(1, n + 1):
    suma = suma + i 


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


#Ciclo for que se repita 3 veces V2
import random

numero_secreto= random.randint
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
    