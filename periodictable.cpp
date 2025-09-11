#include <stdio.h>
#include <string.h>

struct Element {
    int atomicNumber;
    char symbol[5];
    char name[20];
};

void showElement(int num) {
    struct Element elements[] = {
        {1, "H", "Hydrogen"},
        {2, "He", "Helium"},
        {3, "Li", "Lithium"},
        {6, "C", "Carbon"},
        {7, "N", "Nitrogen"},
        {8, "O", "Oxygen"},
        {26, "Fe", "Iron"},
        {79, "Au", "Gold"},
        {82, "Pb", "Lead"},
        {118, "Og", "Oganesson"}
    };
    int size = sizeof(elements) / sizeof(elements[0]);
    for (int i = 0; i < size; i++) {
        if (elements[i].atomicNumber == num) {
            printf("Element Found!\n");
            printf("Atomic Number: %d\n", elements[i].atomicNumber);
            printf("Symbol: %s\n", elements[i].symbol);
            printf("Name: %s\n", elements[i].name);
            return;
        }
    }
    printf("Element not found in database.\n");
}

int main() {
    int num;
    printf("Enter Atomic Number to search: ");
    scanf("%d", &num);
    showElement(num);
    return 0;
}

