SECURE=(('a','@'),('s','$'),('o','0'),('i','1'),('I','|'),('v','^'),('h','#'))
def securePass(pswd):
    for a,b in SECURE:
        pswd=pswd.replace(a,b)
    return pswd
if __name__ == '__main__':
    pas=input("Enter the password which you wanted to convert in a special way\n")
    password=securePass(pas)
    print(f'Your Secure password is {password}')
