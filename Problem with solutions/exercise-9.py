import random
# def funnyName(fname,lname):
#     nlist=[]
#     for i in fname:
#         lname=random.randint(0,+2)
#         print(fname[i],lname)
#     return f'Your name is-> {a} {b}.'

def funnyName(first_name, lastt_name, number):
    for i in range(0, number):
        joumbled_name = first_name[i]+" "+lastt_name[random.randint(0, number-1)]
        print(joumbled_name)

if __name__ == '__main__':
    count=int(input('How many friends do you have-> '))
    lis=[]
    f_name=[]
    l_name=[]
    for i in range(count):
        a=input(f'Enter the name of your {i+1} friend-> ')
        lis.append(a)
    for i in lis:
        i=i.split(' ')
        f_name.append(i[0])
        l_name.append(i[1])
    funnyName(f_name,l_name,count)
