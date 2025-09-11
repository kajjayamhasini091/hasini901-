#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Contact {
    char name[50];
    char phone[15];
};

void addContact() {
    struct Contact c;
    FILE *fp = fopen("phonebook.dat", "ab");
    if (!fp) {
        printf("Error opening file!\n");
        return;
    }
    printf("Enter Name: ");
    scanf(" %[^\n]", c.name);
    printf("Enter Phone: ");
    scanf("%s", c.phone);

    fwrite(&c, sizeof(c), 1, fp);
    fclose(fp);
    printf("Contact Added Successfully!\n");
}

void displayContacts() {
    struct Contact c;
    FILE *fp = fopen("phonebook.dat", "rb");
    if (!fp) {
        printf("No contacts found!\n");
        return;
    }
    printf("\n--- Phone Book ---\n");
    while (fread(&c, sizeof(c), 1, fp)) {
        printf("Name: %s | Phone: %s\n", c.name, c.phone);
    }
    fclose(fp);
}

int main() {
    int choice;
    while (1) {
        printf("\n--- Phone Book ---\n");
        printf("1. Add Contact\n2. Display Contacts\n3. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: addContact(); break;
            case 2: displayContacts(); break;
            case 3: exit(0);
            default: printf("Invalid choice!\n");
        }
    }
    return 0;
}

