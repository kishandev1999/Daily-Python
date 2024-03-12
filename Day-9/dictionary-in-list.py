#PRINT THE STATEMENTS AS PER THE VALUES IN THE DICTIONARY
import os
os.system('cls')
name=input("Enter the country name you visited : ")
visits = int(input(f"how many times you visited {name} : "))
list_of_cities=eval(input(f"Enter the cities you visited in {name} :"))
#eval will take the input which is in list format
#Enter the cities you visited in india :['delhi','punjab']
'''
eval() is evaluate the expressions :
Example: If I gave any list content wrongly, then:
Enter the cities you visited in India :[delhi,p
Traceback (most recent call last):
  File "y:\Python\Day-9\dictionary-in-list.py", line 6, in <module>
    list_of_cities=eval(input(f"Enter the cities you visited in {name} :"))
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 1
    [delhi,p
    ^
SyntaxError: '[' was never closed
'''

travel_log =[
    {
        "country":"France",
        "Visits": 12,
        "cities":["Paris","Lillies","Dijon"]
    },
    {
        "country":"Germany",
        "Visits": 5,
        "cities":["Berlin","Hamburg","Strutgart"]
    }
]

#creating function for new entries to add in travel_log
def add_new_country(country,times_visited,list_of_cities):
    new_country={}
    new_country["country"] = country
    new_country["visits"] = times_visited 
    new_country["cities"] = list_of_cities
    
    travel_log.append(new_country)

add_new_country(name,visits,list_of_cities)  

#print(travel_log)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times")  
print(f"My Favorite city is {travel_log[2]['cities'][0]}")