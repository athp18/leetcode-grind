#include <stdio.h>
#include <stdlib.h>

// my first C program!
char** fizzBuzz(int n, int* returnSize) {
    char** result = (char**)malloc(n * sizeof(char*));
    
    for (int i = 1; i <= n; ++i) {
        if (i % 3 == 0 && i % 5 == 0) {
            result[i-1] = "FizzBuzz";
        } else if (i % 3 == 0) {
            result[i-1] = "Fizz";
        } else if (i % 5 == 0) {
            result[i-1] = "Buzz";
        } else {
            result[i-1] = (char*)malloc(11 * sizeof(char));
            sprintf(result[i-1], "%d", i);
        }
    }
    
    *returnSize = n;
    return result;
}
