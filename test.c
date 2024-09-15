#include <stdio.h>

const char ch = 'x';
int uninit;
int init = 10;

void function() {
    int *ref = &init;
    static int sta_int = 10;
    printf("%c", ch);
}
