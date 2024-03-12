#LISTS IN DICTIONARIES AND DICTIONARIES IN DICTIONARIES
'''
nested_dict={
    key1:[list]
    key2:{dict}
}
'''
captials={
    "India":"New Delhi",
    "Germany":"Berlin",
    "France":"Paris"
}

#LISTS IN DICTIONARIES
travel_log ={"France":
            {"cities_visited":["paris", "Lille","Dijon"], 
             "no_of_visits":4},
             "India": ["Hyderabad","Mumbai","Banglore"]}

#DICTIONARIES IN LIST
travel_log = [
            {
            "country":"France",
            "cities_visited":["paris", "Lille","Dijon"], 
             "no_of_visits":12
             },
            {
             "country":"India",
             "cities_visited": ["Hyderabad","Mumbai","Banglore"]
             }
]

print