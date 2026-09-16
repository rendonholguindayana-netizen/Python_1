'''try:
    
    numero = int(input("Ingrese un número: "))
    print(f"El número ingresado: {numero}")

except ValueError:
    print("Ingrese un número Valido")




menu = 0

while menu != 3:

    try:

        menu = int(input(""" 
        Seleccione una opcion:
        1.Sumar
        2.Restar
        3.Salir
        
        :  """))

        if menu ==1:
            n1=int(input("Ingrese Primer Número: "))
            n2=int(input("Ingrese Segundo Número: "))
            print(f"Resultado {n1+n2}")
        
        elif menu ==2:
            n1=int(input("Ingrese Primer Número: "))
            n2=int(input("Ingrese Segundo Número: "))
            print(f"Resultado {n1-n2}")
        
        else:
            print("Opción Invalida")

    except ValueError:
        print("Inngrese un número valido")

print("Saliendo del sistema")'''


#Ejercicios taller 4:

print("="*30)
# Ejercicio 1: try / except básico

try:
    numero = int(input("Ingrese un número entero: "))
    print(f"El número ingresado es: {numero}")

except ValueError:
    print("Error: debe ingresar un número válido.")


print("="*30)
## Ejercicio 2: División segura con ZeroDivisionError

try:
    dividiendo = float(input("Ingrese el dividiendo: "))
    divisor = float(input("Ingresa el divisor: "))
    resultado = dividiendo / divisor

    print(f"Resultado: {dividiendo} / {divisor} = {resultado}")

except ZeroDivisionError:
    print("Error: no es posible dividir entre cero.")

except ValueError:
    print("Error: ingrese únicamente valores numéricos.")


print("="*30)
# Ejercicio 3: else y finally

try:
    edad = int(input("Ingrese su edad: "))

except ValueError:
    print("Error: la edaddebe ser un nùmero entero.")

else:
    if edad >= 18:
        print("Acceso permitido.")

    else:
        print("Acceso denegado: debe ser mayor de edad.")

finally:
    print("Verificaciòn finalizada.")


print("="*30)
# Ejercicio 4: Solicitar un dato válido hasta que el usuario lo ingrese correctamente:

while True:

    try:
        nota = float(input("Ingrese una nota entre 0.0 y 5.0: "))

        if nota < 0.0 or nota > 5.0:
            raise ValueError("La nota debe estar entre o.o y 5.0.")

        break
    except ValueError as e:
        print(f"Entrada invàlida: {e}. Intente de nuevo.")

print(f"Nota registrada: {nota}") 


print("="*30)
# Ejercicio 5: raise — lanzar una excepción personalizada:

def calcular_promedio(notas):

    if len(notas) == 0:
        raise ValueError("La lista de notas no puede estar vacia.")
    return sum(notas) / len(notas)

try:
    n = int(input("¿Cuàntas notas va a ingresar?: "))
    notas = []

    for i in range(n):
        nota = float(input(f" Nota {i+1}: "))
        notas.append(nota)

    promedio = calcular_promedio(notas)
    print(f"Promedio: {round(promedio, 2)}")

except ValueError as e:
    print(f"Error: {e}.")



