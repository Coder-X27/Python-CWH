operator=int(input('1 for Addition\n2 for Substraction\n3 for Multiplication\n4 for Division\n'))
a=int(input('Enter the first number\n'))
b=int(input('Enter the second number\n'))

if operator==1:
    if a==56 and b==9:
        ans=77
    else:
        ans=a+b
elif operator==2:
    ans=a-b
elif operator==3:
    if a==45 and b==3:
        ans=555
    else:
        ans=a*b
elif operator==4:
    if a==46 and b==6:
        ans=4
    else:
        ans=a/b
else:
    print('Invalid Character !')

print('Then answer is ',ans)