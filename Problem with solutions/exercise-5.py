
def palindrome(n):
    n+=1
    while not is_palindrome(n):
        n+=1
    return n

def is_palindrome(n):
    return str(n)==str(n)[::-1]

number=[1,6,87,43]
for i in range(len(number)):
    if i>10:
        print(f'Next Palindrome for {number[i]} is {palindrome(number[i])}')
    else:
        i=i+0