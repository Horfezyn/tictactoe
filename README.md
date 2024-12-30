# Juego de Tic Tac Toe

## Resumen
Esta es una implementación simple en Python del clásico juego **Tic Tac Toe** como parte del curso de IA impartido por el Dr. Yair Andrade, también conocido como "El Gato". Permite que dos jugadores se turnen para jugar en una cuadrícula de 3x3 hasta que haya un ganador o el juego termine en empate.

## Características
- **Juego por turnos**: Los jugadores alternan turnos usando "X" y "O".
- **Visualización dinámica del tablero**: El tablero se actualiza después de cada movimiento.
- **Detección de ganadores**: Verifica filas, columnas y diagonales para encontrar una combinación ganadora.
- **Detección de empate**: Finaliza el juego si todas las posiciones están ocupadas sin un ganador.

## Cómo Ejecutar

### Requisitos previos
Asegúrate de tener Python 3 instalado en tu sistema. Para verificar, ejecuta:
```bash
python --version
```

### Pasos para ejecutar
1. Copia el código en un archivo Python llamado `tic_tac_toe.py`.
2. Abre una terminal o línea de comandos.
3. Ejecuta el script:
   ```bash
   python tic_tac_toe.py
   ```
4. Sigue las instrucciones en pantalla para jugar.

## Instrucciones de Juego
1. El juego comienza con el jugador "X".
2. Los jugadores se turnan para ingresar un número entre 1-9 correspondiente a la posición en el tablero:

   **Posiciones del Tablero:**
   ```
   1 | 2 | 3
   --+---+--
   4 | 5 | 6
   --+---+--
   7 | 8 | 9
   ```
3. El juego verifica si hay un ganador después de cada movimiento.
4. Si todas las posiciones están ocupadas sin un ganador, el juego declara un empate.

## Desglose del Código

### Funciones Clave
1. **`imprimir_tablero()`**
   - Imprime el estado actual del tablero.

2. **`verificar_ganador()`**
   - Verifica combinaciones ganadoras en filas, columnas y diagonales.

3. **`verificar_empate()`**
   - Comprueba si todas las posiciones del tablero están ocupadas sin un ganador.

4. **Bucle Principal del Juego**
   - Maneja la entrada de los jugadores, actualiza el tablero y verifica ganadores/empates.

### Combinaciones Ganadoras
- **Filas**: [1, 2, 3], [4, 5, 6], [7, 8, 9]
- **Columnas**: [1, 4, 7], [2, 5, 8], [3, 6, 9]
- **Diagonales**: [1, 5, 9], [3, 5, 7]

## Ejemplo de Salida
### Inicio del Juego
```
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
Turno del jugador X
Introduce un número (1-9):
```

### Escenario Ganador
```
X | O | X
--+---+--
X | O | O
--+---+--
O | X | X
El jugador X es la verdura y ha ganado!
```

### Escenario de Empate
```
X | O | X
--+---+--
O | X | O
--+---+--
X | O | X
Ha sido un empate, mala suerte!
```

## Limitaciones Conocidas
- No soporta modo de un solo jugador o IA.
- La validación de entrada está limitada a rango numérico y duplicados.

## Mejoras Futuras
- Añadir un modo de un solo jugador con IA.
- Mejorar la interfaz de usuario con representación gráfica (por ejemplo, Tkinter).
- Agregar funcionalidad para reiniciar el juego.

## Licencia
Este proyecto es libre para usar y modificar.

---
¡Disfruta del juego! 