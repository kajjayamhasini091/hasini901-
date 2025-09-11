#include <stdio.h>

int main() {
    int pin = 1234, enteredPin, option;
    float balance = 5000, amount;

    printf("Enter your PIN: ");
    scanf("%d", &enteredPin);

    if (enteredPin != pin) {
        printf("Incorrect PIN!\n");
        return 0;
    }

    while (1) {
        printf("\n--- ATM Simulator ---\n");
        printf("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &option);

        switch (option) {
            case 1:
                printf("Your Balance: %.2f\n", balance);
                break;
            case 2:
                printf("Enter Deposit Amount: ");
                scanf("%f", &amount);
                balance += amount;
                printf("Amount Deposited Successfully!\n");
                break;
            case 3:
                printf("Enter Withdraw Amount: ");
                scanf("%f", &amount);
                if (amount > balance) {
                    printf("Insufficient Balance!\n");
                } else {
                    balance -= amount;
                    printf("Withdrawal Successful!\n");
                }
                break;
            case 4:
                printf("Thank you for using ATM!\n");
                return 0;
            default:
                printf("Invalid Option!\n");
        }
    }
    return 0;
}

