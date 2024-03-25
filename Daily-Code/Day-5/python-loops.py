'''
LOOPS:

SYNTAX:
FOR LOOP :
for item in list_of_items:
        #DO SOMETHING TO EACH ITEM
'''

fruits=['apple','peach','banana']

for item in fruits:
    print(item)
    print(item + " pie")
    print(fruits)
print(fruits)

#output:
'''
apple
apple pie
['apple', 'peach', 'banana']
peach
peach pie
['apple', 'peach', 'banana']
banana
banana pie
['apple', 'peach', 'banana']
['apple', 'peach', 'banana']
'''

#RANGE
'''
RANGE:

SYNTAX:
for number in range(a,b):
    print(number)
'''

for number in range(1,10):
    print(number)

#OUTPUT : Print all numbers from 1 to 9. [not 10]
'''
1
2
3
4
5
6
7
8
9
'''
#It will check all the numbers from START, TILL END

for number in range(1,10,3):
    print(number)
    
#OUTPUT:
#It will skip the 3 numbers every time within the given range range(1,10,3) abd print the values
'''
1
4
7
10
'''

#EXERCISE:
#SUM ALL 1 TO 100 NUMBERS 
total=0
for num in range(1,101):
    total+=num
print(total)

#OUTPUT:
#5050

