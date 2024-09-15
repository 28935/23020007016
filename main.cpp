
#include <stdio.h>
 
int divide(int a, int b)
{
    return a/b;
}
 
int main()
{
    fprintf(stdout, "input value\n");
    int a = 3, b = 0;
    int div = divide(a, b);
    fprintf(stdout, "div value: %d\n", div);
 
    return 0;
}
