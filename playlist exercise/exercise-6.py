import random as r

i=1;c=0;p=0;d=0
while(i<=10):
    rand=r.randint(1,10)
    if rand<3:
        comp='s'
    elif rand>=3 and rand<6:
        comp='w'
    elif rand>=6 and rand<=10:
        comp='g'

    inp=input('Enter "S" for snake "W" for water and "G" for gun\n')
    
    if comp=='s' and inp=='w':
        print('You Lost! Snake drank all the Water\nYour score is ',i)
        c=c+1
    elif comp=='s' and inp=='w':
        print('You Lost! Snake drank all the Water\nYour score is ',i)
        c=c+1
    elif comp=='w' and inp=='g':
        print('You lost! Your Gun fell down into the water\nYour score is ',i)
        c=c+1
    elif comp=='s' and inp=='g':
        print('You won! You killed the Snake with the gun')
        p=p+1
    elif comp=='w' and inp=='s':
        print('You won! Snake drank all the Water')
        p=p+1
    elif comp=='s' and inp=='g':
        print('You won! You killed the Snake with the gun')
        p=p+1
    elif comp==inp:
        print('Try again! You both Choosed the Same')
        d=d+1
    i=i+1

print(f'You won {p} Times Lost {c} Times and Draw {d} Times')