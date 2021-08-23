import datetime as e
date=str(e.datetime.now())

print('--------->Welcome to the Health Management System<--------')
a=int(input('Enter 1 for Retrieve and 2 for Write\n'))
who=int(input('For which user you wanted to write\nEnter 1 for Karan 2 for Harry and 3 for Kartik\n'))

if a==1:#Mode whether its Retrieve or Write
    choice=int(input('What do you wanted to see\n1 Exercise list 2 Diet\n'))
    if who==1:#Check for which person does this is running
        if choice==1:#Thing you watned to check
            f=open('./exercise-5/karanex.txt')
            print(f.read())
        elif choice==2:
            f=open('./exercise-5/karandi.txt')
            print(f.read())
        else:
            print('Enter a valid character')
    elif who==2:
        if choice==1:
            f=open('./exercise-5/harryex.txt')
            print(f.read())
        elif choice==2:
            f=open('./exercise-5/harrydi.txt')
            print(f.read())
        else:
            print('Enter a valid character')
    elif who==3:
        if choice==1:
            f=open('./exercise-5/karex.txt')
            print(f.read())
        elif choice==2:
            f=open('./exercise-5/kardi.txt')
            print(f.read())
        else:
            print('Enter a valid character')
    else:
        print('Invalid character ! Choose 1, 2 or 3 ')
elif a==2:
    choice=int(input('What do you wanted to write\n1 Exercise list 2 Diet\n'))
    if who==1:#Check for which person does this is running
        if choice==1:#Thing you watned to check
            f=open('./exercise-5/karanex.txt','a')
            ex=input('Enter which exercise did you perform\n')
            f.write('\n['+date+']->'+ex)
        elif choice==2:
            f=open('./exercise-5/karandi.txt')
            ex=input('Enter what did you eat\n')
            f.write('\n['+date+']->'+ex)
        else:
            print('Enter a valid character')
    elif who==2:
        if choice==1:
            f=open('./exercise-5/harryex.txt')
            ex=input('Enter which exercise did you perform\n')
            f.write('\n['+date+']->'+ex)
        elif choice==2:
            f=open('./exercise-5/harrydi.txt')
            ex=input('Enter what did you eat\n')
            f.write('\n['+date+']->'+ex)
        else:
            print('Enter a valid character')
    elif who==3:
        if choice==1:
            f=open('./exercise-5/karex.txt')
            ex=input('Enter which exercise did you perform\n')
            f.write('\n['+date+']->'+ex)
        elif choice==2:
            f=open('./exercise-5/kardi.txt')
            print(f.read())
            ex=input('Enter what did you eat\n')
            f.write('\n['+date+']->'+ex)
        else:
            print('Enter a valid character')
    else:
        print('Invalid character ! Choose 1, 2 or 3 ')

else:
    print('Enter 1 or 2 for valid character')