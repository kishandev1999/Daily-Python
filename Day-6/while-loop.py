'''
WHILE LOOP WILL CONTINUOUSLY RUN WHEN THE CONDITION BECOMES TRUE

SYNTAX:
while something_is_true:
    #DO SOMETHING REPEATEDLY
'''

number_of_hurdles=6
while number_of_hurdles > 0:
    print("Jump")
    number_of_hurdles -=1
    print(number_of_hurdles)
    
#OUTPUT:
'''
Jump
5
Jump
4
Jump
3
Jump
2
Jump
1
Jump
0
'''

#ROBO-HURDLE-WHILE-LOOP
#REFERENCE :
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
#robo-hurdle-while-loop.png



'''
WHILE LOOPS ARE BIT DANGEROUS THAN FOR LOOP
-BECAUSE IN FOR-LOOP YOUR ARE SETTING HOW MANY TIMES THE ITEMS HAS TO ITERATE
-BUT, IN WHILE-LOOP WE ARE SETTING A CONDITIONS AND ASKING TO RUN WHEN THAT CONDITION GOT SATISFIED
- IF WE HAVEN'T SET ANY FALSE CONDITION IN WHILE LOOP, IT WILL RUN CONTINUOUSLY
- THIS MAY LEAD TO INFINITE LOOP
'''

#INFINITE LOOP
'''
while 5 > 3 :  # This is always true
    print("Yes")  #Hence, this statement print continuously
'''
#SO, BE CAREFUL WITH THIS WHILE LOOP :D
    