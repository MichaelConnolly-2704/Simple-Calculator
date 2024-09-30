def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def take_away(x,y):
    return x - y

def divide(x,y):
    if y == 0:
        return "Error! Divison by zero"
    else:
        return x/y
    
def calculator():
    while True:
        print("\n Simple calculator Menu: ")
        print("1 Add")
        print("2.Subtract")
        print("3.Divide")
        print("5. Exit")

        choice = input("Please choose an option (1-5):")

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Please choose the first number"))
                num2 = float(input("Please choose the second number"))
            except ValueError:
                    print(" Invalid input. Please enter a valid number")
                    continue
        if choice == "1":
            print(f"The result is: {add(num1,num2)}")

        elif choice == "2":
            print(f"The result is {subtract(num1,num2)}")

        elif choice == "3":
            print(f"The result is {divide(num1,num2)}")
        
        elif choice == "4":
            print(f" The result is {divide(num1,num2)}")

        elif choice == "5":
            print(" Exiting the calculator. Goodbye!")
            break
        else:
            print ("Invalid choice please choose a valid option between 1 - 5")       

calculator()     
