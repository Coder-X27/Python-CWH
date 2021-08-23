// #include <stdio.h>
// #include <conio.h>

// int main()
// {	
//     float num1,num2;
//     printf("Enter the first num\n");
//     scanf("%f",&num1);
//     printf("Enter the Second num\n");
//     scanf("%f",&num2);
//     char ch;
//     printf("Operation ");
//     scanf("%c",&ch);
//     // printf("%c",ch);
//     switch (ch){
//         case '+':
//             printf("The addition of the two numbers is %f",num1+num2);
//             break;
//         case '-':
//             printf("The Substraction of the two numbers is %f",num1-num2);
//             break;
//         case '/':
//             printf("The Division of the two numbers is %f",num1/num2);
//             break;
//         case '*':
//             printf("The Multiplication of the two numbers is %f",num1*num2);
//             break;
        
//         default:
//             printf("Enter a valid character");
//     }
//     getch();
//     return 0;
// }
#include <stdio.h>
int main() {
  char op;
  int first, second;
  printf("Enter an operator (+, -, *, /): ");
  scanf("%c", &op);
  printf("Enter two operands: ");
  scanf("%d %d", &first, &second);

  switch (op) {
    case '+':
      printf("%d + %d = %d", first, second, first + second);
      break;
    case '-':
      printf("%d - %d = %d", first, second, first - second);
      break;
    case '*':
      printf("%d * %d = %d", first, second, first * second);
      break;
    case '/':
      printf("%d / %d = %d", first, second, first / second);
      break;
    default:
      printf("Error! operator is not correct");
  }

  return 0;
}
