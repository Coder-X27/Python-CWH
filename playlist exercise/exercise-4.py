# Astrological Stars
v=int(input('Enter the Astrological Stars\n'))
while(True):
    a=int(input('Enter 0 or 1 for a binary search\n'))
    if a==0:
        for i in range(v):
            for j in range(i+1):
                print('*', end = "")
            print()
        break
    elif a==1:
        for i in range(v):
            for j in range(v-i):
                print('*', end = "")
            print()
        break
    else:
        print('Invalid number try again')
