#Variables.
#Condicionales.
#Ciclos.
#Manejo de Errores.

#Empresa de bus. Vende tiquetes:

'''    

Medellín -> Bogotá = 120000
Medellín -> Cali = 100000
Medellín -> Barranquilla = 150000
Medellín -> Cartagena = 200000

Proceso compra:

Solicitar:
Destino.
Cantidad de Tiquetes.
Segun la cantidad de tiquetes pedir los nombres de los pasajeros.
Calcular total a pagar.
Mostrar Destino0,los nombres de los pasajeros, total a pagar.


'''

#Ciclo Infinito para que se repita todo el proceso:

while True:
    print("=== TIQUETE DE BUS === \n")
    
    try:
        menu = int(input(''' 
        Seleccione Ruta a comprar:
        1.Medellín - Bogotá
        2.Medellín - Cali
        3.Medellín - Barranquilla
        4.Medellin - Cartagena
        5.Salir '''))

        #Condicional: Verificar que opción escogio la persona

        if menu in range (1,5):
            
            valor_tiquete=0
            if menu ==1:
                valor_tiquete = 120000
                ruta ="Medellín - Bogotá"
            elif menu ==2:
                valor_tiquete = 100000
                ruta ="Medellín - Cali"
            elif menu ==3:
                valor_tiquete = 150000
                ruta ="Medellín - Barranquilla"
            elif menu ==4:
                valor_tiquete = 200000
                ruta ="Medellín - Cartagena"
            
            try:
                cantidad =int(input("Cantidad de tiquetes a comprar: "))
                lista_pasajeros = []
                for i in range(cantidad):
                    pasajero= input(f"Ingrese el nombre del pasajero {i+1} ")
                    lista_pasajeros.append(pasajero)

                #Mostrar todo
                
                print(f''' 
                === RESUMEN COMPRA ===
                -Ruta = {ruta}
                -Cantidad Pasajeros = {cantidad}
                -Valor Tiquete = {valor_tiquete}
                -Valor tiquete = {cantidad*valor_tiquete}
                -Pasajeros = {lista_pasajeros}

                ''')

            except ValueError:
                print("Ingrese una cantidad valida")

        elif menu ==5:
            print("Saliendo del Sistema")
            break

        else:
            print("Opción Invalida.")

    

    except ValueError:
        print("Ingrese una opción Valida.")