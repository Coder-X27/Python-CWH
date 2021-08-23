print("Welcome to the Calculator\nTo use this Insert the number and then press 'Enter' and if you wanted to stop the programme then press 'q' from the keyboard")

sum=0
print('Enter the numbers"->')
while True:
    userInp=input('')
    if userInp!='q':
        sum=sum+int(userInp)
    else:
        print(f"Thank you for using tha calculator your total price is :-> {sum}")
        break