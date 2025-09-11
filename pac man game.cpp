#include <iostream>
#include <conio.h>   // for _getch() on Windows
#include <cstdlib>
#include <ctime>
using namespace std;

const int ROWS = 10;
const int COLS = 20;

char grid[ROWS][COLS+1] = {
    "###################",
    "#C....#.....#.....#",
    "#.##..###..###..#.#",
    "#.....#.......#...#",
    "#.###.#.###.#.###.#",
    "#.....#..G..#.....#",
    "###.#####.#####.###",
    "#.....#.......#...#",
    "#.###.###.#.###.#.#",
    "###################"
};

int pacX = 1, pacY = 1;
int ghostX = 5, ghostY = 8;
int score = 0;

void printGrid() {
    system("cls");
    for (int i = 0; i < ROWS; i++) {
        cout << grid[i] << endl;
    }
    cout << "Score: " << score << endl;
    cout << "Controls: W (up), S (down), A (left), D (right)" << endl;
}

bool movePlayer(char move) {
    int newX = pacX, newY = pacY;

    if (move == 'w' || move == 'W') newX--;
    else if (move == 's' || move == 'S') newX++;
    else if (move == 'a' || move == 'A') newY--;
    else if (move == 'd' || move == 'D') newY++;

    if (grid[newX][newY] == '#') return false; // wall block

    if (grid[newX][newY] == '.') {
        score += 10;
    }

    grid[pacX][pacY] = ' ';
    pacX = newX;
    pacY = newY;
    grid[pacX][pacY] = 'C';
    return true;
}

void moveGhost() {
    int dir = rand() % 4;
    int newX = ghostX, newY = ghostY;

    if (dir == 0) newX--;
    else if (dir == 1) newX++;
    else if (dir == 2) newY--;
    else if (dir == 3) newY++;

    if (grid[newX][newY] == ' ' || grid[newX][newY] == '.') {
        grid[ghostX][ghostY] = ' ';
        ghostX = newX;
        ghostY = newY;
        grid[ghostX][ghostY] = 'G';
    }
}

bool checkWin() {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            if (grid[i][j] == '.') return false;
        }
    }
    return true;
}

int main() {
    srand(time(0));

    printGrid();

    while (true) {
        if (_kbhit()) { // check if key pressed
            char move = _getch();
            movePlayer(move);
        }

        moveGhost();
        printGrid();

        if (pacX == ghostX && pacY == ghostY) {
            cout << "\n?? Game Over! The ghost caught you!\n";
            break;
        }

        if (checkWin()) {
            cout << "\n?? You Win! All dots eaten!\n";
            break;
        }
    }

    return 0;
}

