def fact(n):
    if(n==1):
        return 1
    else:
        f=n*fact(n-1)
        return f
def trailingZeros(n):
    count=0
    i=5
    while n//i!=0:
        count +=int(n/i)
        i*=5
    return count


if __name__ == '__main__':
    num=int(input("Enter the number of which you wanted the factorial"))
    # print(fact(num))
    print(trailingZeros(num))
    