lis=[]
i=1
n=int(input('Enter the number of elements you wanted to be in a list\n'))
while i<=n:
    elem=int(input(f"Enter the {i} element of the list\n"))
    lis.append(elem)
    i+=1
# 1st method 
# lis1 = sorted(lis, reverse = True)
# print(f"\nSort Method returns this List : {lis1}")
lis1=lis[:]
lis1=lis1.reverse()
print(lis1)
# 2nd method
lis2=lis[::-1]
print(f"Slicing Method returns this List : {lis2}")

# 3rd method 
lisr=lis[:]
for i in range(len(lisr)//2):
    lisr[i],lisr[len(lisr)-i-1]=lisr[len(lisr)-i-1],lisr[i]

print(f'The swapping method returns this List : {lisr}\n')
if lis1==lis2 and lis2==lisr:
    print('All the 3 Lists are same')