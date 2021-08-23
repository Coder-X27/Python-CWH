#include <stdio.h>

int main()
{
    int age;
    int VipPass=0;
    VipPass=1;
    printf("Enter your age");
    scanf("%d",&age);

    if(( age <= 70 && age >= 18) ||(VipPass==1) )
    {
        printf("You are above 18 and below 70, So you can drive");
    } 

    else
    {    printf("you cannot drive");
    }
    return 0;
}