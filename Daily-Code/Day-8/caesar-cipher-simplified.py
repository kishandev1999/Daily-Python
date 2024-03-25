import os
from caesar_cipher_logo import logo
os.system('cls')

print(logo)

alphabet=['a','b','c','d','e','f','g','h','i','j','k',
          'l','m','n','o','p','q','r','s','t','u','v',
          'w','x','y','z','a','b','c','d','e','f','g','h','i','j','k',
          'l','m','n','o','p','q','r','s','t','u','v',
          'w','x','y','z']

def cipher(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
        #ex: 5 * -1 = -5
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"Here is the {direction}d result : {end_text}")
 
should_continue = True  
while should_continue:
    direction= input("Type 'decode' for decryption or 'encode' for encryption : ").lower()
    text=input("Enter the text to encrypt the message : ").lower()
    shift=int(input("Type the shift number : "))
    #IF USER ENTERED NUMBER MORE THAN 26, THEN
    shift = shift % 26
    #HERE WE WILL GET 1,2,3 SOON AFTER 26 NUMBERS
    #IF USER ENTERED 27 SHIFTS, THEN 27%26 =1
    #28%26=2, 24%26=24, 29%26=3..........
    
    cipher(start_text=text, shift_amount=shift, cipher_direction=direction)
    #ASK USER TO EXECUTE THE STATEMENTS AGAIN:
    result = input("Type 'yes' if you want to go again. Otherwise type 'no' \n")
    if result == 'no':
        should_continue = False
        print("Good Bye")