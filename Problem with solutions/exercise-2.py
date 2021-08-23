def prog():
    n=int(input('Enter the number of apples you have \n'))
    mn=int(input('Enter the Minimum number to check \n'))
    mx=int(input('Enter the Maximum number to check \n'))
    if mn==mx:
        print('This is not a Range ')
    else:
        for i in range(mn,mx+1):
            if n%i==0:
                print(f'{i} is a divisor of {n}')
            else:
                print(f'{i} is not a divisor of {n}')

if __name__ == '__main__':
    print("Welcome to the Apple Distribution programme")
    prog()