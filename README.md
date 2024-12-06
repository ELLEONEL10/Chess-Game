```markdown
# Python Chess Game with Pygame

A simple chess game built using Python and Pygame. This project implements the core functionality of chess, including piece movements and turn-based gameplay, with a graphical user interface (GUI).

## Features
- Fully playable chess game with GUI.
- Turn-based gameplay for two players.
- Basic rules implemented:
  - Legal moves for each piece.
  - Turn-based logic (White starts first).
- Visual highlights for the board and chess pieces.
- Easy-to-use interface for selecting and moving pieces.

## Screenshots
*(Add screenshots of the game interface here once available, showing the board setup, piece movement, etc.)*

## Getting Started

### Prerequisites
- Python 3.8 or newer installed.
- Pygame library installed.

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/chess-game.git
   cd chess-game
   ```

2. **Install the dependencies:**
   ```bash
   pip install pygame
   ```

3. **Ensure the `images/` folder contains all the required chess piece images:**
   - `white_pawn.png`, `black_pawn.png`, etc.
   - Download recommended images from [Chessboard.js PNGs](https://github.com/davidbau/chessboardjs/tree/master/img/chesspieces/wikipedia).

4. **Run the game:**
   ```bash
   python chess_game.py
   ```

---

## How to Play
1. Launch the game.
2. The board displays the standard chess setup. White plays first.
3. **To make a move:**
   - Left-click on a piece to select it.
   - Left-click on a valid destination square to move it.
4. Turns alternate between players after each valid move.
5. The game continues until a player declares checkmate (manual end for now).

---

## Folder Structure
```
chess-game/
├── chess_game.py       # Main Python script
├── images/             # Folder for chess piece images
│   ├── white_pawn.png
│   ├── black_pawn.png
│   ├── ...
├── README.md           # Project documentation
```

---

## Planned Enhancements
- Add support for **check** and **checkmate** detection.
- Implement advanced chess rules:
  - **Castling**
  - **En passant**
  - **Pawn promotion**
- Include basic **AI** for single-player mode.
- Add a **save/load game** feature.
- Improve the **GUI** with animations.

---

## Contributing
Contributions are welcome! If you’d like to contribute, please follow these steps:
1. **Fork the repository.**
2. **Create a new branch**
3. **Commit your changes.**
4. **Submit a pull request.**

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Creators
- **Fadi Abbara** – Developer and Creator
- **Anas Zahran** – Developer and Creator
