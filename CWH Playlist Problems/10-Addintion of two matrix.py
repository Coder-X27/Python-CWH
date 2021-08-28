col=int(input('Enter the number of Columns in the matrix\n'))
row=int(input('Enter the number of Rows in the matrix\n'))
size=col*row
mat1=[]
mat2=[]
result=[]
print("Enter the elements For the First Matrix")
for i in range(size):
    a=int(input(f'{i+1} Element-> '))
    mat1.append(a)
print("Enter the elements For the Second Matrix")
for i in range(size):
    a=int(input(f'{i+1} Element-> '))
    mat2.append(a)
i=0
while i<size:
    p=mat1[i]+mat2[i]
    result.append(p)
    i+=1

print('The additon of the two matrix are ',result)
