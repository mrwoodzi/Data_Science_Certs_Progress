#include <stdio.h>
#include <stdlib.h>  // Include the standard library for memory management functions

int main() {
    // Define the number of elements in the array
    int num_elements = 6;

    // Dynamically allocate memory for an array of integers
    int* the_numbers = (int*)malloc(num_elements * sizeof(int));

    // Check if memory allocation was successful
    if (the_numbers == NULL) {
        printf("Memory allocation failed. Exiting.\n");
        return 1;
    }

    // Initialize the dynamically allocated array
    for (int i = 0; i < num_elements; i++) {
        the_numbers[i] = i * 10; // Assign some example values
    }

    // Declare and initialize a variable 'zork' to 0
    int zork = 0;

    // Print the initial value of 'zork'
    printf("Before the loop, zork is: %d\n", zork);

    // Loop through the dynamically allocated array
    for (int i = 0; i < num_elements; i++) {
        // Increment 'zork' by 1
        zork = zork + 1;

        // Print the current value of 'zork' and the current element from the array
        printf("Iteration %d: zork is now %d, the_numbers[%d] is %d\n", i, zork, i, the_numbers[i]);
    }

    // Print the final value of 'zork'
    printf("After the loop, zork is: %d\n", zork);

    // Free the dynamically allocated memory to avoid memory leaks
    free(the_numbers);

    return 0;
}
