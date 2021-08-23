#include<stdio.h>

int main()
{
int a ,n=4 ,factorial=1;
for(a=1;a<=n;a++)
{
    factorial *=a;
}
printf("The factorial of %d is %d",n,factorial);
return 0;
}