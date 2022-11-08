/*
 * malloc.c
 */

#include <stdio.h>
#include <stdlib.h>

char *foo(void);
char *baz(void);

int main(int argc, char *argv[])
{
    char *t;
    char *x;

    x = baz();
    t = foo();

    printf("my string says \"%i\"\n", t);
    printf("my string says \"%i\"\n", x);


    free(t);
    free(x);
}

char *foo(void)
{
    char *s;

    s = malloc(6);
    if(s == NULL) {
        printf("error allocating memory\n");
        exit(1);
    }
    *s = 'h';
    *(s+1) = 'e';
    *(s+2) = 'l';
    *(s+3) = 'l';
    *(s+4) = 'o';
    *(s+5) = '\0';


    return s;
}

char *baz(void)
{
    char *y;

    y = malloc(30);
    if(y == NULL) {
        printf("error allocating memory\n");
        exit(1);
    }
    int i = 47;
    while(i > 1){
        *(y + 47 - i) = 'h';
        /*printf("i: \"%i\"\n", i);
        */
        i = i - 1;
    }
    *(y + i) = '\0';

    return y;
}
