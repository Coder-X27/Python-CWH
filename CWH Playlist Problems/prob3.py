def seperator(a):
    for i in a:
        i=i.split('\t')
        rate.append(i[1])
        mat=i[0]
        currency.append(mat)

if __name__ == '__main__':
    currency=[]
    rate=[]
    with open('currency.txt') as f:
        a=f.readlines()
    print('Enter the amount of money you wanted to see in other currencies:-> ')
    money=int(input())
    seperator(a)
    print(currency)
    print(rate)
    i=0
    while i<53:
        print(f'{currency[i]} is equals to {money*float(rate[i])} Rupees')
        i+=1