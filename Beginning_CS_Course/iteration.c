#include <stdio.h>

int main() {
    // Declare an array of numbers
    int the_numbers[] = {9, 41, 12, 3, 74, 15};

    int zork = 0;

    // Print the initial value of 'zork'
    printf("Before the loop, zork is: %d\n", zork);

    // Loop through the array 'the_numbers'
    for (int iter = 0; iter < 6; iter++) {
        // Increment 'zork' by 1
        zork = zork + 1;

        // Print the current value of 'zork' and the current element from the array
        printf("Iteration %d: zork is now %d, the_numbers[%d] is %d\n", iter, zork, iter, the_numbers[iter]);
    }

    // Print the final value of 'zork'
    printf("After the loop, zork is: %d\n", zork);

    return 0;
}


// int the_numbers[] = {9, 41, 12, 3, 74, 15};
// declares an integer array named the_numbers and initializes it with the 
// specified values. This is equivalent to a Python list in terms of storing 
// a collection of values, but there are some important differences to note:
// Static Size: In C, you need to specify the size of the array when declaring 
// it. In this case, the array has a fixed size of 6 elements. Python lists, on 
// the other hand, can dynamically resize as you add or remove elements.
// Data Type: C arrays are strongly typed, meaning they can only store elements 
// of the declared data type, which is int in this case. Python lists can hold 
// elements of different data types in the same list.
// Zero-Based Indexing: Like Python lists, C arrays use zero-based indexing, so 
// the first element is the_numbers[0], the second is the_numbers[1], and so on.
// Mutability: While Python lists are mutable (you can change their elements), 
// C arrays are fixed in size and cannot be resized or changed once created.
// In Python, the equivalent code to create a list with the same elements would be:
// python
// Copy code
// the_numbers = [9, 41, 12, 3, 74, 15]
// So, while both C arrays and Python lists can store a collection of values, they 
// have differences in terms of size, data types, mutability, and indexing.
    // Declare and initialize a variable 'zork' to 0

// Loop through the array 'the_numbers': This is a comment line that provides a description of the 
// purpose of the following code. It indicates that the code inside the loop will iterate through the
//  elements of the the_numbers array.
// for (int iter = 0; iter < 6; iter++) {: This is the start of a for loop, which is used to perform 
// a set of actions repeatedly. Here's a breakdown:

// for: This keyword indicates the beginning of a loop structure.
// (int iter = 0; iter < 6; iter++): This is the loop header, which defines the loop's control parameters. 
// Let's dissect this:
// int iter = 0;: This is an initialization statement. It declares an integer variable named iter and 
// initializes it to 0. The iter variable will be used to control the loop.
// iter < 6;: This is the loop condition. The loop will continue executing as long as the condition 
// iter < 6 is true. In this case, the loop will run as long as iter is less than 6.
// iter++: This is the increment statement. After each iteration of the loop, it increases the value 
// of iter by 1. This step is executed at the end of each loop iteration.
// {: This curly brace marks the beginning of the code block that belongs to the for loop. All 
// statements within this block are part of the loop and will be executed repeatedly as long as the 
// loop condition is met.

// zork = zork + 1;: This is the code within the loop. Let's break it down:

// zork: This is a variable that was declared before the loop. It is being used to keep track of the 
// number of loop iterations.
// =: This is the assignment operator, which assigns a new value to the variable on the left.
// zork + 1;: This expression calculates the new value of zork. It takes the current value of zork, 
// adds 1 to it, and assigns the result back to zork.
// So, this for loop will start with iter set to 0. It will continue iterating as long as iter is less 
// than 6. During each iteration, it increments the zork variable by 1 and updates the iter variable.
// When iter reaches 6 or more, the loop terminates.

// This loop effectively counts the number of iterations, and the zork variable will hold the count of 
// iterations when the loop finishes.