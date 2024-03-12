#CALCULATOR
import os
os.system("cls")
from calculator_logo import logo
print(logo)

#ADDITION
def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1+n2

def div(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

def calculator():
    num1=float(input("Enter the number : "))
    for symbols in operations:
        print(symbols)
    
    should_continue = True
    
    while should_continue:
        operator_symbol=input("Pick up the operation from above line : ")
        num2=float(input("Enter the other number : "))
        #getting the value from the dictionary her based on the operations
        calculation_function=operations[operator_symbol]
        #print(calculation_function)
        '''
        operator=+
        operations[+] will be 'add'
        so, calculation_function is equal to 'add'
        '''
        answer = calculation_function(num1, num2)
        """
        So, calculation_function(num1,num2) will be like
        add(num1,num2)
        """
        print(f"{num1} {operator_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1=answer
        else:
            should_continue = False
            os.system('cls')
            #CALLING INSIDE THE FUNCTION
            calculator() #RECURSIVE
            #BE CAREFUL WITH THIS: WHENEVER YOU MISS ANY INDENT, IT WILL RUN RECURSIVELY
            


calculator()
        





