#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int balance = 1000, bet, guess, number;

    srand(time(0));

    printf("?? Welcome to Casino Game ??\n");
    printf("Your starting balance: %d\n", balance);

    while (balance > 0) {
        printf("\nEnter your bet amount (0 to quit): ");
        scanf("%d", &bet);

        if (bet == 0) {
            printf("Thanks for playing! Final balance: %d\n", balance);
            break;
        }
        if (bet > balance) {
            printf("Not enough balance!\n");
            continue;
        }

        printf("Guess a number between 1 and 10: ");
        scanf("%d", &guess);

        number = rand() % 10 + 1;

        if (guess == number) {
            printf("?? Correct! You win %d\n", bet * 2);
            balance += bet * 2;
        } else {
            printf("? Wrong! The number was %d\n", number);
            balance -= bet;
        }
        printf("Current balance: %d\n", balance);
    }

    if (balance <= 0) {
        printf("?? You lost all money! Game Over.\n");
    }
    return 0;
}

