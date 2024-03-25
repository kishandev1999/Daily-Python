#EXERCISE
'''
PRINT("THANK YOU FOR CHOOSING PIZZA PYTHON DELIVERY SERVICES")
BASED ON THE USER ORDER PRINT THE BILL
SMALL PIZZA : 15$
MEDIUM PIZZA : 20$
LARGE PIZZA : 25$
ADD PEPPERONI FOR SMALL : +2$
ADD PEPPERONI FOR MEDIUM AND LARGE : +3$
ADD EXTRA CHEESE FOR ANY SIZE : +1$
'''
size = input("Enter the size of your PIZZA : ")
add_pepperoni = input("You want pepperoni? Y OR N")
extra_cheese = input("You want extra_cheese?  Y OR N")
print("THANK YOU FOR CHOOSING PIZZA PYTHON DELIVERY SERVICES")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
    
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is : ${bill}")