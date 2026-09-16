
"""#Repaso clase pasada
var_nombre= input("Por favor ingrese su nombre: ")

#Variable numerica (int = numero entero float= decimales)
var_edad =int(input(f"{var_nombre} Por favor ingresa tu edad: "))
if var_edad >= 18 :
    print(f"{var_nombre} Usted es mayor de edad")

else:
    print(f"{var_nombre} Usted es menor de edad")
# Validar si la edad es > = 18. y mostrar un mensaje que diga que es mayor

if var_edad >= 18 :
    print(f"{var_nombre} Usted es mayor de edad")

else:
    print(f"{var_nombre} Usted es menor de edad")
    
if var_edad <= 17 :
    print(f"{var_nombre} Usted es menor de edad")

else:
    print(f"{var_nombre} Usted es mayor de edad")


# Ejercicio 1: Determinar si un número es positivo, negativo o cero

numero = float(input("Por favor ingrese un número: "))

#Validar tres opciones: Positivo, negativo o cero

if numero > 0: #Opcion 1: Validar si es Positivo 
 print(f"El numero: {numero} es positivo")

elif numero <0: #Opcion 2: Validar si es negativo
    print(f"El numero : {numero} es negativo")

else:
    print(f"El numero : {numero} es cero") 

# Ejercicio 3: Determinar si un número es par o impar

numero = float(input("Por favor ingrese un número: "))

if numero % 2 != 0:
    print(f"El numero {numero} es Impar")

else:
    print(f"El numero {numero} es Par")

# Ejercicio 4: Clasificar una nota académica

nota = float(input("Ingrese la nota obtenida (0.0 a 5.0): "))

if nota >5.0:
    print("Nota invalida")

elif nota >= 4.5:
    print("Desempeño superior")

elif nota >= 3.5:
     print("Desempeño alto")

elif nota >= 3.0:
    print("Desempeño básico")

elif nota >=0:
    print("Desempeño bajo")

else:
    print("Nota invalida")"""


# Ejercicio 5: Determinar el mayor de tres números

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))

if n1 == n2 and n2 == n3:
    mayor ="Números iguales"

elif n1 >= n2 and n1 >= n3:
    mayor = n1

elif n2 >= n1 and n2 >= n3:
    mayor = n2

print(f"El mayor de los tres números es: {mayor}")

