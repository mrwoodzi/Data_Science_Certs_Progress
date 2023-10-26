#include <stdio.h>  // Include the standard input/output library

int main() {
    // Declare and initialize an integer variable 'x' with the value 32
    int x = 32;

    // Declare a character array (string) 'y' and initialize it with "hello world"
    // Memory allocation for the string 'y' including space for each character and the null terminator
    char y[] = "hello world";

    // Print the value of 'x' and the string 'y'
    // The 'x' variable is printed using the %d format specifier for integers
    // The 'y' string is printed using the %s format specifier for strings
    printf("%d %s\n", x, y);
    printf("%d %s", x, y);
    printf(" %d %s", x, y);

    // Note: Memory allocation for 'x' and 'y' is automatic and managed by C,
    // and you don't need to worry about manual memory allocation or deallocation.

    return 0;  // Return 0 to indicate successful program execution
}
