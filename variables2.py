 # Ejercicio 1: Suma de dos números

print("="*30)
print("Ejercicio 1: Suma de dos números")

numero1=float(input("ingrese el primer número:"))
numero2=float(input("ingrese el primer número:"))

suma=numero1 + numero2

print(f"la suma es: {suma}")

# Ejercicio 2: Área de un rectángulo

print("="*30)
print("Ejercicio 2: Área de un rectángulo")


base = float(input("ingrese la base del rectangulo:"))
altura = float(input("ingrese la altura del rectangulo: "))

area = base*altura # fórmula: base × altura

print("El área del rectangulo es:", area)

# Ejercicio 3: Conversión de minutos a horas y minutos

print("="*30)
print("Ejercicio 3: Conversión de minutos a horas y minutos")


minutos_totales = int(input("ingrese la cantidad de minutos:"))

hora = minutos_totales // 60 # división entera → horas completas
minutos = minutos_totales % 60 # módulo → minutos restantes

print(minutos_totales, "minutos equivalen a", hora,"horas y", minutos,"minutos")

# Ejercicio 4: Cálculo del precio con descuento

print("="*30)
print("Ejercicio 4: Cálculo del precio con descuento")

precio = float(input("ingrese el pprecio del producto: "))
descuento =float(input("ingrese el porcentaje del promedio: "))

valor_descuento = precio *(descuento/100) # valor que se descuenta
precio_final = precio - valor_descuento  # precio con descuento

print("El precio final a pagar es:", precio_final)


# Ejercicio 5: Intercambio de valores entre dos variables

print("="*30)
print("Ejercicio 5: Intercambio de valores entre dos variables")

a= float(input("ingrese el valor de a: "))
b= float(input("ingrese el valor de b: "))

auxiliar = a # guardar temporalmente el valor de a
a=b  # a toma el valor de b
b=auxiliar  # b toma el valor original de a

print("Después del intercambio: a= ", a, ",b=",b)


#Ejercicio para resolver:

print("="*30)
print("Ejercicio 1: Calcular perimetro de terreno rectangular")

largo = float(input("ingrese la base: "))
ancho = float(input("ingrese el ancho: "))

perimetro= 2*(largo+ancho)

print("El perimetro del terreno es: ", perimetro)


print("="*30)
print("Ejercicio 2: calcular promedio")

nota1 = float(input("ingrese nota 1: "))
nota2 = float(input("ingrese nota 2: " ))
nota3 = float(input("ingrese nota 3: "))

promedio = (nota1+nota2+nota3)/3

print("Su promedio es: ", promedio)

print("="*30)
print("Ejercicio 4: solicitar nombre y mensaje de presentación")

nombre= "Dayana"
edad= 18
vivo= "medellin"

print(f"Hola, mi nombre es {nombre}, tengo {edad} años y vivo en {vivo} ")

print("="*30)
print("Ejercicio 5: solicitar valores")

pesos= float(input("ingrese el valor para convertir de pesos Col a Dollar: "))
dollar= pesos/4000

print(f"Total de dolares: {dollar}")


print("="*30)
print("Ejercicio 6:convertidor de segundos")


