
# Chess AI Project
Welcome to my Chess AI project! This application features a fully functional chess GUI with move validation and legal move highlighting.

## 🧠 Engine Performance
This Mini-Max Chess AI will play at a rating of around 600 ELO based on Chess.com.

## 🚀 Getting Started

Follow these instructions to set up the environment and run the chess engine on your local machine.

### 1. Prerequisites
Before you begin, ensure you have the following installed:
* **Visual Studio Code (VS Code)**: [Download here](https://code.visualstudio.com/)
* **Python**: [Download here](https://www.python.org/downloads/)

### 2. Project Setup

1.  **Open the Project**: Launch Visual Studio Code and open the folder containing this project.
2.  **Python Extension**:
    * If you are opening this project for the first time, a prompt may appear in the bottom right asking to install the **Python Extension**.
    * Click **Yes/Install**. This is highly recommended for IntelliSense (code completion) and easier troubleshooting.

### 3. Install Dependencies

You need to install the `pygame` library to render the graphical interface.

1.  Open the Terminal in VS Code (`Ctrl + ~` or go to **Terminal > New Terminal**).
2.  Run the installation command for your operating system:

**For Windows:**
```bash
pip install pygame
```
### 4. Running the Chess AI
   
1.  To start playing against the AI, you need to execute the main.py file located within the source directory.
2.  game_mode = 0 means human plays white while game_mode = 1 means computer plays white, depth is the deepness of the minimax tree (default is 2).
3.  Navigate to the root directory of the project in your terminal.
4.  Execute the script using the following command:
```bash
python src/main.py
```
Note: Ensure you are running the command from the project root (the folder containing the src directory) so that the engine can correctly locate the game assets and modules.
