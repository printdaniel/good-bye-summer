from entry_manager import DataEntry

good_bye =""" 
    _____                 _        ____                _____                                     
  / ____|               | |      |  _ \              / ____|                                    
 | |  __  ___   ___   __| |______| |_) |_   _  ___  | (___  _   _ _ __ ___  _ __ ___   ___ _ __ 
 | | |_ |/ _ \ / _ \ / _` |______|  _ <| | | |/ _ \  \___ \| | | | '_ ` _ \| '_ ` _ \ / _ \ '__|
 | |__| | (_) | (_) | (_| |      | |_) | |_| |  __/  ____) | |_| | | | | | | | | | | |  __/ |   
  \_____|\___/ \___/ \__,_|      |____/ \__, |\___| |_____/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                         __/ |                                                  
                                        |___/                                                   """ 
menu = """
1 Mostrar variables
2 Leer Base de datos
3 Ingresar variables de hoy
4 Salir
"""
print(good_bye)
print(menu)
data = DataEntry()

if __name__ == '__main__':
    opciones = {1: data.variables, 2: data.mostrar_todos, 3: data.entrada_datos, 4: 'finalizado'}
    opcion = int(input("Eliga una opción: "))
    while True:
        if opcion not in opciones:
            print("Eliga una opción entre 1 y 4")
            opcion = int(input("Eliga una opción: "))
        elif opciones[opcion] == 'finalizado':
            print("Programa finalizado")
            break
        else:
            opciones[opcion]()
            opcion = int(input("Eliga una opción: "))
