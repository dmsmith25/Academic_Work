/*
 * part3_memory_addresses.c
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{

    // Create variables to represent items in the heap and the stack
    char *heap_mem = malloc(6);
    int stack_val = 0;
    int *stack_mem = &stack_val;

    // Print out where the instructions, heap, and stack are stored in memory
    printf("Instructions in Mem: %p\n", main);
    printf("Heap in Mem: %p\n", heap_mem);
    printf("Stack in Mem: %p\n", stack_mem);


}
