#PROJECT
'''
TAKE THE INPUT FROM THE USER:
- HOW MANY LETTERS WOULD YOU LIKE IN YOUR PASSWORD?
- HOW MANY SYMBOLS WOULD YOU LIKE IN YOUR PASSWORD?
- HOW MANY NUMBERS WOULD YOU LIKE IN YOUR PASSWORD?
BASED ON THE INPUT : GENERATE THE PASSWORD
'''

#solution:
import random

letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
         'K', 'L','M', 'N', 'O', 'P', 'Q', 'R','S', 
         'T', 'U', 'V', 'W', 'X','Y', 'Z']

numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','/','<','>',':']
print("Welcome to the PY PASSWORD GENERATOR")
rq_password_len = int(input('WHAT WOULD BE THE LENGTH OF YOUR PASSWORD?'))
rq_symbols=int(input("HOW MANY SYMBOLS WOULD YOU LIKE IN YOUR PASSWORD"))
rq_numbers=int(input("HOW MANY NUMBERS WOULD YOU LIKE IN YOUR PASSWORD?"))

password_char_list=[letters,numbers,symbols]

final_password=[]

if rq_password_len <= (rq_symbols+rq_numbers)+1:
    print("YOUR PASSWORD CONSISTS MINIMUM 2 ALPHABETS")
#elif rq_password_len =< rq_symbols+rq_numbers:
#    print("YOUR PASSWORD CONSISTS MINIMUM 2 ALPHABETS")
else:
    range_of_password_char = rq_password_len-rq_symbols-rq_numbers
    # print(range_of_password_char)
    
    for i in range(range_of_password_char):
        random_alphabets=random.choice(letters)
        #print(random_alphabets,end="")
        final_password.append(random_alphabets)
    
    for j in range(rq_numbers):
        random_numbers=random.choice(numbers)
        #print(random_numbers,end="")
        final_password.append(random_numbers)
        
    for k in range(rq_symbols):
        random_symbols=random.choice(symbols)
        #print(random_symbols,end="") 
        final_password.append(random_symbols)
        
#print(f"{random_alphabets}{random_numbers}{random_symbols}")
#print(final_password)
random.shuffle(final_password)
#print(*final_password,end="")

for item in final_password:
    print(item,end="")









'''
range_of_password_char = rq_password_len-rq_symbols-rq_numbers
print(range_of_password_char)

if (rq_password_len) == (range_of_password_char+rq_numbers+rq_symbols):
    print(rq_password_len)
    print(range_of_password_char+rq_numbers+rq_symbols)
    print("satisfied")
else:
    print("not satisfied")

for i in range(range_of_password_char):
    random_alphabets=random.choice(letters)
    print(random_alphabets,end="")

for j in range(rq_numbers):
    random_numbers=random.choice(numbers)
    print(random_numbers,end="")

for k in range(rq_symbols):
    random_symbols=random.choice(symbols)
    print(random_symbols,end="") 
'''

