def palindrome(n):
    n+=1
    while not is_palindrome(n):
        n+=1
    return n

def is_palindrome(n):
    return str(n)==str(n)[::-1]

cases=int(input('Enter the number of Cases-> '))
number=[]
for i in range(cases):
    num=int(input('Enter the number-> '))
    number.append(num)
for i in range(num):
    print(f'Next Palindrome for {number[i]} is {palindrome(number[i])}')