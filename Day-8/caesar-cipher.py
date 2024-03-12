import os
os.system('cls')
alphabet=['a','b','c','d','e','f','g','h','i','j','k',
          'l','m','n','o','p','q','r','s','t','u','v',
          'w','x','y','z','a','b','c','d','e','f','g','h','i','j','k',
          'l','m','n','o','p','q','r','s','t','u','v',
          'w','x','y','z']
direction= input("Type 'decode' for decryption or 'encode' for encryption : ").lower()
text=input("Enter the text to encrypt the message : ").lower()
shift=int(input("Type the shift number : "))

#ENCRYPTION FUNCTION
def encrypt(plain_text,shift_amount):
    cipher_text=""
    word_length = len(plain_text)
    for i in range(word_length):
        letter_index = alphabet.index(plain_text[i])
        shift_index = letter_index + 5
        cipher_text += (alphabet[shift_index])
    print(cipher_text)
        
    

#DECRYPTION FUNCTION
def decrypt(cipher_text,shift_amount):
    plain_text=""
    word_length = len(cipher_text)
    for i in range(word_length):
        letter_index = alphabet.index(cipher_text[i])
        shift_index = letter_index - 5
        plain_text += (alphabet[shift_index])
    print(plain_text)
        
    

#
if direction == "encode":
    encrypt(plain_text=text,shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text,shift_amount=shift)    
else:
    print("WRONG PARAMETER..!")

