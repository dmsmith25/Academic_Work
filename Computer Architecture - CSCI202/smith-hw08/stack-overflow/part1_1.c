/*
 * part1.c
 */
#include <stdio.h>
int foo(); /* function prototype */

int main(int argc, char *argv[])
{
    //printf("x is %d\n", x);

    int x = foo();

    return x;
}

int foo()
{
    int t = 1048576;
    foo();

    return t;

}

