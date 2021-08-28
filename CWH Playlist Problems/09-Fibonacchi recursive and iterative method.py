# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
def fib(n):
    prevnum=0
    currentnum=1
    for i in range(1,n):
        prevprevnum=prevnum
        prevnum=currentnum
        currentnum=prevnum+prevprevnum
    return currentnum


if __name__ == '__main__':
    num=int(input('Enter a number \n'))
    f=fib(num)
    print(f"The Fibonacchi value of the number is {f}")

    