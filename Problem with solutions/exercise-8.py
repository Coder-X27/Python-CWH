import random 
def table(num):
    lis2=[]
    for i in range(10):
        t=num*(i+1)
        lis2.append(t)
    return lis2
def rohanMul(num):
    lis1=[]
    for i in range(10):
        t=num*(i+1)
        if i==4:
            t=num*(i+1)+random.randint(1,num)
        lis1.append(t)
    return lis1
def validator(right,fake):
    i=0
    while i<=10:
        if right[i]!=fake[i]:
            index=i
            return index
            break
        i+=1
if __name__ == '__main__':
    num=int(input('Enter the table you watned to print\n'))
    wrong=rohanMul(num)
    correct=table(num)
    v=validator(correct,wrong)
    print(f"Rohan Das list->{wrong}\nValidator list is->{correct}\nThere is a wrong table at index {v}")
    