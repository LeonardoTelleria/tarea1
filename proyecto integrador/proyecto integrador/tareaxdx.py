import json #json funciona para guardar y cargar datos
import os #os funciona para verificar si un archivo ya existe

transacciones = [] #se define una lista global que almacenara todos los movimiento financeros,
#ingresos y gastos como diccionarios

def cargarD():     #se define una función para cargar los datos desde el archivo 
    global transacciones # se usa global para modificar la variable global la cual es transacciones
    if os.path.exists("gastos_familiares.json"):    #se verifica que el archivo exista
        with open("gastos_familiares.json", "r") as archivo:       #abre el archivo en modo lectura usando read
            transacciones = json.load(archivo)      #se carga el contenido del archivo json a la lista definida
    else:#si el archivo no existe no pasa nada
        pass
#se define la funcion guardar datos
def guardarD():                                                  #se abre el archivo en modo escritura con write
    with open("gastos_familiares.json", "w") as archivo:         # <---si no existe lo crea y si si existe lo sobre escribe
        json.dump(transacciones, archivo, indent=4) #convierte la lista en formato json
#indent=4 lo hace mas legible

def agregarIng():               #se hace una funcion para agregar los ingresos
    try:                #se usa un bloque try-except para manejar posibles errores
        cantidad = float(input("Ingresa la cantidad del ingreso: $"))
        descripcion = input("Ingresa una descripción para el ingreso: ")
        transaccion = {
            "tipo": "ingreso",              #se crea un diccionario transaccion para guardar los datos que se ingresen
            "cantidad": cantidad,
            "descripcion": descripcion
        }
        transacciones.append(transaccion)       #se agregan los datos a la lista global
        print(f" Ingreso de ${cantidad:.2f} añadido correctamente")
    except ValueError:#salta si el usuario no elije el valor correcto
        print(" Por favor, ingresa una cantidad numérica válida")

def agregar_gasto():        #se crea una funcion para agregar gastos
    print("\n--- Categorías de Gastos ---") #se definen las categorias de los gastos a ingresar
    categorias = ["Alimentos", "Transporte", "Vivienda", "Entretenimiento", "Otros"]
    for i, cat in enumerate(categorias, 1): #enumerate recorre la lista por indice y elemento
        print(f"{i}. {cat}")#muestra las categorias
    
    try: #se hace un bloque try para errores de entrada
        opcion_cat = int(input("Elige una categoría (número): "))
        if 1 <= opcion_cat <= len(categorias): #busca que la opcion elegida este en el rango de categorias
            categoria_elegida = categorias[opcion_cat - 1]#como python lee desde 0 se utiliza -1 para que lea desde 1
            cantidad = float(input(f"Ingresa la cantidad del gasto para '{categoria_elegida}': $"))
            descripcion = input("Ingresa una descripción para el gasto: ")
            
            transaccion = {
                "tipo": "gasto",
                "cantidad": cantidad,           #se crea un diccionario para el gasto y su categoria
                "descripcion": descripcion,
                "categoria": categoria_elegida
            }
            transacciones.append(transaccion) #se vuelve a agregar a la lista global
            print(f" Gasto de ${cantidad:.2f} en '{categoria_elegida}' añadido")
        else:#aparece cuando el usuario no elije bien su opcion
            print(" Opción de categoría no válida")
    except (ValueError, IndexError):#salta si el ususario no ingresa bien el la cantidad
        print(" Entrada no válida. Asegúrate de ingresar un gasto real")

def mostrarR():     #se crea otra funcion para mostrar los resultados
    ingresosT = 0.0#el 0.0 es un valor guardado que se ira actualizando con forme el usuario agregue datos
    gastosDC = {
        "Alimentos": 0.0,
        "Transporte": 0.0,
        "Vivienda": 0.0,
        "Entretenimiento": 0.0,
        "Otros": 0.0
    }

    for t in transacciones:         #itera sobre cada transaccion en la lista global
        if t["tipo"] == "ingreso": #si el tipo de transaccion es ingreso, suma la cantidad a los ingresosT
            ingresosT += t["cantidad"]
        elif t["tipo"] == "gasto":  #si el tipo es es gasto suma a la categoria correspondiente de gastosDC
            categoria = t["categoria"]
            gastosDC[categoria] += t["cantidad"]

    gastos_totales = sum(gastosDC.values()) #se calcula el total de los gastos
    
    print("\n--- Resumen de Gastos ---")
    for categoria, total in gastosDC.items():#devuelve la clave y el valor del diccionario
        if total > 0:
            print(f"- {categoria}: ${total:.2f}") #imprime el resultado

    balance = ingresosT - gastos_totales#se calcula el balance final
    print("\n--- Balance Total ---")
    print(f" Ingresos Totales: ${ingresosT:.2f}")
    print(f" Gastos Totales: ${gastos_totales:.2f}")
    print(f" Balance Final: ${balance:.2f}")
    
    if balance > 0:#se muestra un mensaje segun el resultado del balance
        print("Felicitaciones. Estás gestionando bien tu dinero")
    elif balance < 0:
        print("Cuidado. Tus gastos superan a tus ingresos")
    else:
        print("Tus ingresos y gastos están equilibrados ")

def main_menu(): #se define el main para cargar los datos, si existen 
    cargarD()
    while True: #se crea un bucle infinito para mantener el programa en ejecucion  
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Agregar un nuevo ingreso")
        print("2. Agregar un nuevo gasto")
        print("3. Ver resumen y balance")
        print("4. Salir del programa")
        
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == "1":
            agregarIng() #se usan if elif y esle para ejecutar la funcion que se elija 
        elif opcion == "2":
            agregar_gasto()
        elif opcion == "3":
            mostrarR()
        elif opcion == "4":
            guardarD()#se guardan los datos antes de salir del bucle
            break #se rompe el blucle
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 4")# salta si el usuario no elige ninguna opcion que se le indica

if __name__ == "__main__":# se ejecuta el programa completo
    main_menu()