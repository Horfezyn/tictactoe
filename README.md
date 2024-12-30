# Tic Tac Toe Game

## Overview
This is a simple Python implementation of the classic **Tic Tac Toe** game, also known as "El Gato." It allows two players to take turns and play on a 3x3 grid until there is a winner or the game ends in a draw.

## Features
- **Turn-based Gameplay**: Players alternate turns using "X" and "O."
- **Dynamic Board Display**: The board updates after every move.
- **Winner Detection**: Checks rows, columns, and diagonals for a winning combination.
- **Draw Detection**: Ends the game if all positions are filled without a winner.

## How to Run

### Prerequisites
Ensure you have Python 3 installed on your system. To check, run:
```bash
python --version
```

### Steps to Run
1. Copy the code into a Python file named `tic_tac_toe.py`.
2. Open a terminal or command prompt.
3. Run the script:
   ```bash
   python tic_tac_toe.py
   ```
4. Follow the on-screen instructions to play the game.

## Gameplay Instructions
1. The game starts with Player "X."
2. The players take turns entering a number between 1-9 corresponding to the position on the board:

   **Board Positions:**
   ```
   1 | 2 | 3
   --+---+--
   4 | 5 | 6
   --+---+--
   7 | 8 | 9
   ```
3. The game checks for a winner after each move.
4. If all positions are filled without a winner, the game declares a draw.

## Code Breakdown

### Key Functions
1. **`imprimir_tablero()`**
   - Prints the current state of the board.

2. **`verificar_ganador()`**
   - Checks for winning combinations in rows, columns, and diagonals.

3. **`verificar_empate()`**
   - Checks if all board positions are filled without a winner.

4. **Main Game Loop**
   - Handles player input, board updates, and winner/draw detection.

### Winning Combinations
- **Rows**: [1, 2, 3], [4, 5, 6], [7, 8, 9]
- **Columns**: [1, 4, 7], [2, 5, 8], [3, 6, 9]
- **Diagonals**: [1, 5, 9], [3, 5, 7]

## Example Output
### Game Start
```
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
Turno del jugador X
Introduce un número (1-9):
```

### Winning Scenario
```
X | O | X
--+---+--
X | O | O
--+---+--
O | X | X
El jugador X es la verdura y ha ganado!
```

### Draw Scenario
```
X | O | X
--+---+--
O | X | O
--+---+--
X | O | X
Ha sido un empate, mala suerte!
```

## Known Limitations
- Does not support AI or single-player mode.
- Input validation is limited to numeric range and duplicates.

## Future Enhancements
- Add single-player mode with AI.
- Improve user interface with graphical representation (e.g., Tkinter).
- Add replay functionality.

## License
This project is free to use and modify.

---
Enjoy the game!