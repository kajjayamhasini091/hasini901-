#include <stdio.h>

char board[3][3] = { {'1','2','3'}, {'4','5','6'}, {'7','8','9'} };

void printBoard() {
    printf("\n");
    for (int i = 0; i < 3; i++) {
        printf(" %c | %c | %c \n", board[i][0], board[i][1], board[i][2]);
        if (i < 2) printf("---|---|---\n");
    }
    printf("\n");
}

int checkWin() {
    for (int i = 0; i < 3; i++) {
        if (board[i][0]==board[i][1] && board[i][1]==board[i][2]) return 1;
        if (board[0][i]==board[1][i] && board[1][i]==board[2][i]) return 1;
    }
    if (board[0][0]==board[1][1] && board[1][1]==board[2][2]) return 1;
    if (board[0][2]==board[1][1] && board[1][1]==board[2][0]) return 1;
    return 0;
}

int main() {
    int move, player = 1;
    char mark;
    int movesCount = 0;

    while (1) {
        printBoard();
        mark = (player == 1) ? 'X' : 'O';
        printf("Player %d, enter your move (1-9): ", player);
        scanf("%d", &move);

        int row = (move-1)/3;
        int col = (move-1)%3;

        if (move < 1 || move > 9 || board[row][col]=='X' || board[row][col]=='O') {
            printf("Invalid move! Try again.\n");
            continue;
        }

        board[row][col] = mark;
        movesCount++;

        if (checkWin()) {
            printBoard();
            printf("?? Player %d wins!\n", player);
            break;
        } else if (movesCount == 9) {
            printBoard();
            printf("It's a draw!\n");
            break;
        }

        player = (player == 1) ? 2 : 1;
    }
    return 0;
}

