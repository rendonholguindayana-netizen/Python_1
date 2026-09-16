print("=== Tienda Merca + 🏪 ==0\n")

#Solicitar variables

producto = input("Ingrese el nombre del producto: ")
cantidad = int(input(f"Ingrese la cantidad del producto: "))
precio = float(input("Ingrese el precio unitario del producto: "))

#Crear Variables para Calcular.

subtotal = cantidad * precio
iva = subtotal * 0.19
total = subtotal + iva

print("\n === RESUMEN DE COMPRA === \n")

print(f"""
-producto................{producto}
-candidad................{cantidad}
-precio unitario.........{precio}
-subtotal................{subtotal}
-IVA(19%)................{iva}
-Total a pagar...........{total}
""")

#Preguntar si quiere incluir propina
propina = input("¿Desea incluir propina? : ")

if propina == "si" or propina == "SI" or propina == "Si" :
    valor_propina = subtotal * 0.10
    total_final = total + valor_propina

    print(f"""
    -subtotal................{subtotal}
    -Valor Propina...........{valor_propina}
    -IVA(19%)................{iva}
    -Total a pagar...........{total_final}
    """)

elif propina == "no" or propina == "NO" or propina == "No" :
    print("Gracias por su compra TACAÑO")

else:
    print("Opcion no válida, por favor ingrese si o no ") 


print("="*30)

#Ejercicios 1 taller 2:

print("Notas finales de los estudiantes")

variable_nombre = input("Por favor ingrese su nombre: ")
var_calificacion = float(input("Ingrese su calificacion: "))

if var_calificacion >= 4.5 and var_calificacion <=5.0 :
    resultado = "Aprobo"
    desempeño = "Excelente"
    print(f"Estudiantes: {variable_nombre} Calificacion: {var_calificacion} Resultado: {resultado} Desempeño: {desempeño}")

elif var_calificacion >= 3.5 and var_calificacion < 4.5 :
    resultado = "Aprobo"
    desempeño = "Bueno"
    print(f"Estudiantes: {variable_nombre} Calificacion: {var_calificacion} Resultado: {resultado} Desempeño: {desempeño}")

elif var_calificacion >= 3.0 and var_calificacion < 3.5 :
    resultado = "Aprobado"
    desempeño = "Aceptable"
    print(f"Estudiantes: {variable_nombre} Calificacion: {var_calificacion} Resultado: {resultado} Desempeño: {desempeño}")

elif var_calificacion >= 0.0 and var_calificacion < 3.0 :
    resultado = "Reprobo"
    desempeño = "Insuficiente"
    print(f"Estudiantes: {variable_nombre} Calificacion: {var_calificacion} Resultado: {resultado} Desempeño: {desempeño}")

else:
    print(f"{var_calificacion} es invalida")



print("="*30)

# Ejercicio 2:

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad < 0 :
    print("Error: favor ingrese una edad valida")

elif edad >= 18 :
    print("Es mayor de edad")

else:
    faltan = 18 - edad
    print("Es menor de edad")
    print(f"Le faltan {faltan} años para ser mayor de edad")



print("="*30)

#Ejercicio 3:solicitar variable 

nombre = input("Ingrese su nombre: ")
valor_compra = float(input("Ingrese valor de compra "))

#3 Validar que el valor de la compra sea mayor a cero 

if valor_compra <= 0:
    print("\nError: El valor de la compra debe ser mayor a cero")    
else: 
    #calcular el porcentaje de descuento según los rangos
    if valor_compra < 100000:
        porcentaje_descuento = 0
    elif valor_compra < 300000: # Equivalente a "hasta 299.999"
        porcentaje_descuento = 10
    elif valor_compra < 500000: # Equivalente a "hasta 499.999"
        porcentaje_descuento = 15
    else: # $500.000 o más
        porcentaje_descuento = 20

    # 4. Realizar los cálculos matemáticos
    valor_descontado = valor_compra * (porcentaje_descuento / 100)
    total_pagar = valor_compra - valor_descontado

    # 5. Mostrar los resultados finales al usuario
    print(f"\n--- Resumen de la factura para {nombre} ---")

    # Se usa :,.2f para dar formato de moneda con separador de miles y 2 decimales

    print(f"Valor original de la compra:...${valor_compra:,.2f}")
    print(f"Porcentaje de descuento:.......${porcentaje_descuento}%")
    print(f"Valor descontado:..............${valor_descontado:,.2f}")
    print(f"Total a pagar:.................${total_pagar:,.2f}")


print("="*30)

#Ejercio 4:

nombre_ciudad = input("Ingrese el nombre de su ciudad: ")
temperatura = float(input("Ingrese la temperatura actual en grados Celsius: "))

if temperatura < 10 :
    clasificacion = "Muy fría"
    recomendacion = "Se recomienda abrigarse bien."
    print(f"En {nombre_ciudad} hace mucho frio, se recomienda abrigarse bien.")

elif temperatura > 10 and temperatura < 17 :
    clasificacion = "Fría"
    recomendacion = "Se recomienda usar abrigo."
    print(f"En {nombre_ciudad} hace frio, se recomienda usar abrigo.")

elif temperatura >= 18 and temperatura <= 25 :
    clasificacion = "Templada"
    recomendacion = "Se recomienda usar ropa ligera."
    print(f"En {nombre_ciudad} hace templado, se recomienda usar ropa ligera.")

elif temperatura >= 26 and temperatura <= 32 :
    clasificacion = "Caliente"
    recomendacion = "Se recomienda usar ropa fresca e hidratarse bien."
    print(f"En {nombre_ciudad} hace calor, se recomienda usar ropa fresca e hidratarse bien.")

elif temperatura > 32 :
    clasificacion = "Muy caliente"
    recomendacion = "Se recomienda usar ropa lijera, hidratarse muy bien y evitar los rayos del sol."
    print(f"En {nombre_ciudad} hace mucho calor, se recomienda usar ropa lijera, hidratarse muy bien y evitar los rayos del sol.")




print("="*30)

#Ejercicio 5: Datos del empleado

nombre = input("Ingrese el nombre del empleado: ")
horas = float(input("Ingrese las horas trabajadas: "))
valor_hora = float(input("Ingrese el valor de cada hora: "))

#Validar
if horas <= 0 or valor_hora <= 0:
    print("Los valores deben ser positivos")

else:
    #Horas normales y extra
    if horas <= 160:
        horas_normales = horas
        horas_extra = 0

    else:
        horas_normales = 160
        horas_extra = horas - 160

    #Pago de horas
    pago_normal = horas_normales * valor_hora
    pago_extra = horas_extra * valor_hora * 1.25

    #Salario bruto
    salario_bruto = pago_normal + pago_extra

    #Descuento
    descuento = salario_bruto * 0.08

    #Salario neto
    salario_neto = salario_bruto - descuento

    #Mostrar resultados
    print(f"""
    -Empleado: {nombre}
    -Horas normales:{horas_normales}
    -Horas extra:{horas_extra}
    -Pago hora normal:{valor_hora}
    -Pago hora extra:{valor_hora * 1.25}
    -Salario bruto:{salario_bruto}
    -Descuento: {descuento}
    -Salario neto: {salario_neto}
""")