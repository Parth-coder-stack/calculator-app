#Simple Calculator

def add(a,b):
    return a + b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    if a==0 or b==0:
        return "Error,cannot evaluate it"
    else:
        return a/b

#main menu

while True:
    print("\n")
    print("-----------Simple Calculator----------")
    print("1.To add numbers")
    print("2.To subtract numbers")
    print("3.To multiply numbers")
    print("4.To divide numbers")
    ch=input("Enter the choice you want to display ")

    a=int(input("Enter first number "))
    b=int(input("Enter second number "))

    if ch=="1":
        print(f"Result:{add(a,b)}")
    elif ch=="2":
        print(f"Result:{subtract(a,b)}")
    elif ch=="3":
        print(f"Result:{multiply(a,b)}")
    elif ch=="4":
        print(f"Result:{division(a,b)}")
    else:
        break


        
