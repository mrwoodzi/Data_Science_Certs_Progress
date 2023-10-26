#include <stdio.h>

int main() {
    // Declare and initialize an integer variable 'x' with the value 5
    int x = 5;
    // Declare and initialize an integer variable 'y' with the value 0
    int y = 0;

    // Loop and subtract 1 from 'x' until 'x' is equal to 0
    while (x > 0) {
        printf("%d\n", x);  // Print the value of 'x' to the console
        x = x - 1;  // Subtract 1 from 'x'
        if (y < x) {
            printf("Lather\n");
            printf("Rinse\n");
            printf("Repeat\n");
        }
    }
    printf("Blastoff!\n");  // Print "Blastoff!" to the console

    return 0;  // Return 0 to the operating system
}


