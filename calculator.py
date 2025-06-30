# Basic Calculator System

# What this Calculator can do
# Addition, Subtraction, Multiplication, and Division
# Take input from the user
# Display the result

#--------------------------------------

#Function for addition
def add(a,b):
    return a+b

#Function for subtraction
def sub(a,b):
    return a-b

#Function for multiplication
def multiply(a,b):
    return a*b

#Function for division
def divide(a,b):
    if b==0:
        return "Cannot divide by zero"
    return a/b
    
if __name__ == "__main__":
        
    while True:
                
        #Start of the program
        print("Welcome to the calculator")
    
        #Display menu
        print("Select operation:\n 1. Add\n 2. Sub\n 3. Multiply\n 4. Divide")
    
        #Get user's choice
        choice = input("Enter choice (1/2/3/4): ")
        
        #Get number from user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        #Call the appropriate function based on user input
        if choice == '1':
            print("Result: ", add(num1,num2))
        elif choice == '2':
            print("Result: ", sub(num1,num2))
        elif choice == '3':
            print("Result: ", multiply(num1,num2))
        elif choice == '3':
            print("Result: ", divide(num1,num2))
        else:
            print("Invalidnchoice")
        
        count = input("Do you want to continue? (y/n): ")
        if count.lower() != 'y':
            break