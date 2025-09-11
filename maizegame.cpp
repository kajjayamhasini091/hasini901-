#include <iostream>
#include <conio.h>   // for _getch() on Windows
using namespace std;

const int ROWS = 10;
const int COLS = 20;

char maze[ROWS][COLS+1] = {
    "###################",
    "#P   #       #    #",
    "# # ### ### ### # #",
    "# #     #   #   # #",
    "# ##### # # # ### #",
    "#     # # # #     #",
    "### # ### ### ### #",
    "#   #     #     # #",
    "# ### ### # ### #E#",
    "###################"
};

int playerX = 1, playerY = 1;

void printMaze() {
    system("cls"); // clear screen
    for (int i = 0; i < ROWS; i++) {
        cout << maze[i] << endl;
    }
}

int main() {
    char move;
    printMaze();

    while (true) {
        move = _getch(); // get user input (WASD keys)
        int newX = playerX;
        int newY = playerY;

        if (move == 'w' || move == 'W') newX--;
        else if (move == 's' || move == 'S') newX++;
        else if (move == 'a' || move == 'A') newY--;
        else if (move == 'd' || move == 'D') newY++;

        if (maze[newX][newY] == ' ' || maze[newX][newY] == 'E') {
            maze[playerX][playerY] = ' '; // remove old position
            playerX = newX;
            playerY = newY;
            maze[playerX][playerY] = 'P';
        }

        printMaze();

        if (maze[playerX][playerY] == 'E') {
            cout << "\n?? Congratulations! You reached the exit!\n";
            break;
        }
    }
    return 0;
}

