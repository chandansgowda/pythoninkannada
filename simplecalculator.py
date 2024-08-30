import time as t
print("\t\t\t-->> SIMPLE CALCULATOR <<--\n")
t.sleep(0.5)
print("\t\t\t    MENU: ")
print("1.Addition\t2.Subtraction\t3.Multiplication\t4.Division")
t.sleep(0.5)
def func():
    choice = int(input("Enter Your Choice: "))
    if(choice==1):
        add()
    elif(choice==2):
        sub()
    elif(choice==3):
        mul()
    elif(choice==4):
        div()
    else:
        print("Invalid  option!")
        func()

def add():
    a1 = int(input("How many numbers do you want to add: "))
    if(1==a1):
        print("One number can't be added")
        print("Please Re-enter")
        t.sleep(0.5)
        add()
    elif(2==a1):
        n1 = float(input("Enter 1st Number: "))
        n2 = float(input("Enter 2nd Number: "))
        print("Calculating...")
        t.sleep(0.5)
        print("Sum =", n1+n2)
        q()
    else: 
        li_sum = []
        print("Enter Numbers: ")
        for i in range(0,a1):
            li_sum.append(float(input()))
        print("Calculating...")
        t.sleep(0.5)
        sum = 0 
        for val in li_sum:
            sum += val
        print("Sum:", sum )
        q()
        
def sub():
    a1 = int(input("How many numbers do you want to subtract: "))
    if(1==a1):
        print("One number can't be subtracted")
        print("Please Re-enter")
        sub()
    elif(2==a1):
        n1 = float(input("Enter 1st Number: "))
        n2 = float(input("Enter 2nd Number: "))
        print("Calculating...")
        t.sleep(0.5)        
        print("Difference =", n1-n2)
        q()
    else: 
        li_diff = []
        print("Enter Numbers: ")
        for i in range(0,a1):
            li_diff.append(float(input()))
        print("Calculating...")
        t.sleep(0.5)
        diff = 0 
        for val in li_diff:
            diff -= val
        print("Difference:", diff)
        q()

def mul():
    a1 = int(input("How many numbers do you want to multiply: "))
    if(1==a1):
        print("One number can't be multiplied")
        print("Please Re-enter")
        sub()
    elif(2==a1):
        n1 = float(input("Enter 1st Number: "))
        n2 = float(input("Enter 2nd Number: "))
        print("Calculating...")
        t.sleep(0.5)
        print("Product =", n1*n2)
        q()
    else: 
        li_mul = []
        print("Enter Numbers: ")
        for i in range(0,a1):
            li_mul.append(float(input()))
        print("Calculating...")
        t.sleep(0.5)
        mul = 1 
        for val in li_mul:
            mul *= val
        print("Product:", mul)
        q()
    
def div():
    a1 = int(input("How many numbers do you want to divide: "))
    if(1==a1):
        print("One number can't be divided")
        print("Please Re-enter")
        sub()
    elif(2==a1):
        n1 = float(input("Enter 1st Number: "))
        n2 = float(input("Enter 2nd Number: "))
        print("Calculating...")
        t.sleep(0.5)        
        print("Quotient =", n1/n2)
        q()
    else: 
        li_divi = []
        print("Enter Numbers: ")
        for i in range(0,a1):
            li_divi.append(float(input()))
        print("Calculating...")
        t.sleep(0.5)
        divi = li_divi[0]
        for val in range(1,len(li_divi)):
            divi = divi/li_divi[val]
        print("Quotient:", divi)
        q()
    
def q():
    yn1 = input("Go To Main Menu:(y/n): ").lower()
    if(yn1 == 'y'):
        print("")
        func()
        t.sleep(0.5)
    elif(yn1 == 'n'):
        print("Thank you for using our service.")
        t.sleep(0.5)
        exit()
    else:
        print("Invalid Option, Try Again...")
        q()

func()
