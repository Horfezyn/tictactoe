# Inicializar el tablero
tablero = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] #Creamos un arreglo con los numero del 1 al 9
jugador_actual = "X" #Establecemos al primero jugador como X
ganador = False #Establecemos que no hay un ganador

# Función para Imprimir el tablero - la usaremos siempre que se tenga que imprimir los valores del tablero
def imprimir_tablero():
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
    print("--+---+--") #Creamos el patron de separación del tablero
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
    print("--+---+--")
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])

# Función para verificar si hay un ganador
def verificar_ganador():
    # Combinaciones ganadoras, según wikipedia xD
    combinaciones = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
                     (0, 4, 8), (2, 4, 6)]  # Diagonales
    for a, b, c in combinaciones: #Recorremos el arreglo porobando si hay X u O en las posiciones ganadoras.
        if tablero[a] == tablero[b] == tablero[c]:
            return True
    return False

# Función para verificar si hay empate
def verificar_empate():
   return all(pos in ["X", "O"] for pos in tablero) #Creamos una función generadora que verifica las X y O en el array

# Función del ciclo normal del juego
while not ganador:
    imprimir_tablero()
    print(f"Turno del jugador {jugador_actual}")

    # Leer la entrada del jugador
    while True:
        pos = input("Introduce un número (1-9): ")
        if pos.isdigit() and 1 <= int(pos) <= 9: #Verificamos que sea un numero y que esté dentro del rango del gato
            pos = int(pos) - 1
            if tablero[pos] not in ["X", "O"]:
                tablero[pos] = jugador_actual
                break
            else:
                print("Esta posición ya está ocupada. Selecciona otra.")
        else:
            print("Entrada inválida. Introduce un número del 1 al 9.")

    # Verificar si hay un ganador
    if verificar_ganador():
        imprimir_tablero()
        print(f"El jugador {jugador_actual} es la verdura y ha ganado!")
        ganador = True
    elif verificar_empate():
        imprimir_tablero()
        print("Ha sido un empate, mala suerte!")
        break
    else:
        # Cambiar de jugador
        jugador_actual = "O" if jugador_actual == "X" else "X"