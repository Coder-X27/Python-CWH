def lcm(a,b):
    maxnum=max(a,b)
    while True:
        if maxnum%a==0 and maxnum%b==0:
            break
        maxnum=maxnum+1
    return maxnum

if __name__ == '__main__':    
    a=int(input('Enter First number\n'))
    b=int(input('Enter Second number\n'))
    p=(a*b)/lcm(a,b)
    print(f'The LCM of the number {a} ,{b} is:-> {lcm(a,b)} and,')
    print(f'The HCF of the number {a} ,{b} is:-> {p}')