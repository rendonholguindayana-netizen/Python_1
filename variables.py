# ============================================================
# INTRODUCCIÓN A LAS VARIABLES EN PYTHON
# ============================================================

# Una variable permite almacenar un dato para utilizarlo
# posteriormente dentro del programa.

nombre= "Dayana"
documento = 123
direccion = "Medellin"
tiene_deudas = True #variable Booleano : True o False


# ============================================================
# MOSTRAR EL CONTENIDO DE UNA VARIABLE
# ============================================================

print(nombre)



# ============================================================
# CONCATENACIÓN USANDO ,
# ============================================================
print("\nCONCATENACIÓN USANDO ,")
print("=" * 30)

# Al utilizar comas, Python permite mostrar diferentes
# tipos de datos sin necesidad de convertirlos a string.

print("Mi nombre es: ", nombre, "Mi documento es: ", documento)

#Tarea: Mostrar nombre, documento, direccion y tiene_deuda

print ("Mi nombre es: ",nombre,
"Mi documento es: ", documento,
"Mi direccion es: ",direccion,
"Tengo Deudas:", tiene_deudas)

# ============================================================
# CONCATENACIÓN USANDO F-STRINGS
# ============================================================
print("\nCONCATENACIÓN USANDO F-STRINGS")
print("=" * 30)

# Las f-strings permiten insertar variables directamente
# dentro de un texto.
#
# Se coloca la letra f antes de las comillas y las variables
# se escriben entre llaves { }.

print(f"Mi nombre es: {nombre} Mi documento: {documento} Mi direccion: {direccion} Tengo deudas: {tiene_deudas}")

# ============================================================
# F-STRINGS CON COMILLAS SIMPLES
# ============================================================

# También podemos utilizar tres comillas simples (''')
# para crear textos de varias líneas.
print("=" * 30)


print(f"""
Nombre: {nombre}
Documento: {documento}
Direccion: {direccion}
¿Tiene deudas: {tiene_deudas}         
""")

# SALTO DE LÍNEA EN PYTHON

# \n representa un salto de línea.
# Salto de línea al inicio del texto

print(f"n Hola, {nombre}!")
