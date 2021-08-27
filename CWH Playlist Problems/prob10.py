def count(num):
    a=0
    while num>0:
        x=num%10
        num=(num/10).__floor__()  
        a+=1
    return a

if __name__ == '__main__':
    num=int(input('Enter the number\n'))
    const=num
    r=0
    n=count(num)
    while num>0:
        x=num%10
        r=r+pow(x,n)
        num=(num/10).__floor__()        

    if const==r:
        print(f'This is an ArmStrong number.s')
    else:
        print(f'This is not an ArmStrong number.s')