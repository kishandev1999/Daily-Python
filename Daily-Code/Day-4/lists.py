#LISTS
#REFERENCE : https://docs.python.org/3/tutorial/datastructures.html
fruits = ['apple', 'banana', 'orange']
#           0        1          2          <- ORDER OR INDEX OF THE LIST
states_of_india=['Andhra', 'TamilNadu','Maharastra','orrisa','West Bengal', 'Gujarat', 'kerala']


print(states_of_india[0]) #output: Andhra
print(states_of_india[1]) #output : TamilNadu
#print(states_of_india[<offSet>]) 


#REVERSE INDEXING :
#COUNT FROM REVERSE ORDER
print(states_of_india[-1]) #output: kerala

#ALTER THE ITEMS IN THE LIST
states_of_india[0] = "Andhra Pradesh"
print(states_of_india) #This will change 0 index element "Andhra" to "Andhra Pradesh"

#ADD A NEW ITEM IN THE LIST
states_of_india.append('karnataka') #This will add at the end of the list

#ADD MORE THAN 2 ELEMENTS AT A TIME IN THE LIST
states_of_india.extend(['uttar Pradesh', 'Jarkhand']) #This will add at the end of the list

#INDEX OUT OF RANGE:
print(states_of_india[50])
#This is through you an error because, it's index is not in range of 50

#NESTED LISTS
fruits=['apple','banana','orange','pineapple','papaya']
vegetables=['potato','carrot','tomato','cauliflower']

dizzy_dozen = [fruits,vegetables]
print(dizzy_dozen)
#output:
[['apple','banana','orange','pineapple','papaya'],['potato','carrot','tomato','cauliflower']]

print(dizzy_dozen[1][1])
#output: carrot

 
