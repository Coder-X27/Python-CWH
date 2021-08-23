def agechecker(age,year):
    if age>400:
        if year-age>100:
            print('You seems to be the oldest person alive !')
        elif age>year: 
            print('You are not yet born')
        else:
            year=age+100
            print(f'You will be 100 years old in {year}.')
    else:   
        if age>100:
            print('You seems to be the oldest person alive !')
        elif age<=0:
            print('You are not yet born')
        else:
            year=year-age+100
            print(f'You will be 100 years old in {year}.')

if __name__ == '__main__':
    age=int(input('Enter your age or year of birth\n'))
    year=2021
    agechecker(age,year)