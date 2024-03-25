def prime_checker(number):
    is_prime= True
    for i in range(2,number):
        if number % i == 0:
            is_prime= False
        
    if is_prime:
        print("PRIME NUMBER")
    else:
        print("NOT A PRIME NUMBER")            
            
user_number = int(input("Enter the number : "))            
prime_checker(user_number)