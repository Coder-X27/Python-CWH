#include<stdio.h>
int main()
{
    int i=0;
do{
    printf("The value is %d \n",i++);
    if(i==15)
    {
        break;
    }
}while(i<20);
return 0;
}