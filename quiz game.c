#include <stdio.h>

int main() {
    int choice, score = 0;

    printf("*********************************\n");
    printf("       Welcome to Quiz Game!     \n");
    printf("*********************************\n\n");

    // Question 1
    printf("Q1. What is the capital of India?\n");
    printf("1. Mumbai\n2. New Delhi\n3. Kolkata\n4. Chennai\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);
    if (choice == 2) {
        printf("? Correct!\n\n");
        score++;
    } else {
        printf("? Wrong! Correct answer is 2. New Delhi\n\n");
    }

    // Question 2
    printf("Q2. Who is known as the father of C language?\n");
    printf("1. James Gosling\n2. Bjarne Stroustrup\n3. Dennis Ritchie\n4. Guido van Rossum\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);
    if (choice == 3) {
        printf("? Correct!\n\n");
        score++;
    } else {
        printf("? Wrong! Correct answer is 3. Dennis Ritchie\n\n");
    }

    // Question 3
    printf("Q3. Which data type is used to store characters in C?\n");
    printf("1. int\n2. float\n3. char\n4. double\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);
    if (choice == 3) {
        printf("? Correct!\n\n");
        score++;
    } else {
        printf("? Wrong! Correct answer is 3. char\n\n");
    }

    // Question 4
    printf("Q4. Which symbol is used to end a statement in C?\n");
    printf("1. , (comma)\n2. . (dot)\n3. ; (semicolon)\n4. : (colon)\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);
    if (choice == 3) {
        printf("? Correct!\n\n");
        score++;
    } else {
        printf("? Wrong! Correct answer is 3. ; (semicolon)\n\n");
    }

    // Question 5
    printf("Q5. What is the result of 5/2 in C?\n");
    printf("1. 2.5\n2. 2\n3. 3\n4. Error\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);
    if (choice == 2) {
        printf("? Correct!\n\n");
        score++;
    } else {
        printf("? Wrong! Correct answer is 2. 2 (integer division)\n\n");
    }

    // Final Result
    printf("*********************************\n");
    printf(" Your final score is: %d out of 5\n", score);
    printf("*********************************\n");

    if (score == 5) {
        printf("?? Excellent! You got all correct!\n");
    } else if (score >= 3) {
        printf("?? Good job! You passed!\n");
    } else {
        printf("?? Better luck next time!\n");
    }

    return 0;
}

