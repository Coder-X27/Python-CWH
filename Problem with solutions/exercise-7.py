def statements(lis,st):
    item1=lis[0].split(' ')
    item2=lis[1].split(' ')
    item3=lis[2].split(' ')    
    matcher(item1,st)
    matcher(item2,st)
    matcher(item3,st)
    if matcher(item1,st)>matcher(item2,st) and matcher(item1,st)>matcher(item2,st):
        print(f'The highest count of {st} is {matcher(item1,st)} in {item1}.')
    elif matcher(item2,st)>matcher(item1,st) and matcher(item2,st)>matcher(item3,st):
        print(f'The highest count of {st} is {matcher(item2,st)} in {item2}.')
    else:
        print(f'The highest count of {st} is {matcher(item3,st)} in {item3}.')
        
def matcher(lis,st):
    count=0
    for i in lis:
        if i==st:
            count+=1
    # print('The count is ',count)
    return count

if __name__ == '__main__':    
    lis=['This is good','python is good','python is not python snake']
    st=input('Enter something for search-> ')
    statements(lis,st)