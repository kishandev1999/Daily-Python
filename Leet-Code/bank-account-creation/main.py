'''
'user_name': 'kishan dev',
                             'phone_no': '6304508114', 
                             'city': 'kakinada', 
                             'amount': 100, 
                             'account_no': 33367549224
'''

import random
from logo import welcome_logo,logo
class Bank():
    def __init__(self):
        self.customers_data={}
        self.customers_list=[{'user_name': 'kishan dev',
                             'phone_no': '6304508114', 
                             'city': 'kakinada', 
                             'amount': 100, 
                             'account_no': 33367549224},
                             {'user_name': 'satish', 
                              'phone_no': 7173741515,
                              'city': 'kkd', 
                              'amount': 500, 
                              'account_no': 27318394610}]
    
    
    def welcome_note(self):
        print(welcome_logo)
        print(logo)
    
    
    #ASK THE OPTIONS    
    def select_options(self):
        print('''CHOOSE THE OPTIONS TO BEGIN : \n
              1. TO CREATE AN ACCOUNT
              2. TO CHECK THE BALANCE
              3. TO DEPOSIT THE MONEY
              4. TO WITHDRAW THE MONEY''')
        option=input("Enter your option (1/2/3/4) : ")
        return option
    
    #Checking the bank account exists or not:
    def account_check(self):
        account_no_check= int(input("Enter your account number : "))
        for i in self.customers_list:
            #print(i)
            if i['account_no'] == account_no_check:
                print("Account already exits")
                return i
            '''    
            else:
                print("Account is not exists.")
                continue_flow=input("Please type 'Y' to create an account, 'N' to exit : " ).lower()
                if continue_flow == 'y':
                    self.create_account()
                elif continue_flow == 'n':
                    print("Thank you for using our services \n Please reach us again \n ***HAVE A GREAT DAY*** ")
                else:
                    print("***INVALID INPUT***")
            '''
    
    #CREATE THE ACCOUNT        
    def create_account(self):
        print("***** CREATE YOUR ACCOUNT *****")
        self.customers_data['user_name']=input("Enter your name : ")
        self.customers_data['phone_no']=input("Enter phone number : ")
        self.customers_data['city']=input("Enter your city : ")
        self.customers_data['amount']=input("How much you want to deposit :")
        account_no=random.randint(100000000,99999999999)
        #print(f"Your account number is : {account_no}")
        self.customers_data['account_no']=account_no
        print(self.customers_data)
        self.customers_list.append(self.customers_data)
        print(self.customers_list)
     
     #CHECK THE BALANCE:
    def check_balance(self):
        print(self.customers_data)
        
    def deposit_money(self):
        print("***** DEPOSIT YOUR MONEY*****")
        self.account_check()
        single_customer_value=self.account_check()
        
        amount_insert=input("Enter your amount to deposit : ")
        single_customer_value['amount']+=int(amount_insert)
        print(f"*****Your deposit amount is {amount_insert} *****")
        check_balance_again=input("type 'Y' to check your balance, 'N' to quit : ").lower()
        if check_balance_again=='y':
            self.check_balance()
        else:
            print("Thank you for using our services \n Please reach us again \n ***HAVE A GREAT DAY*** ")
        
    
        
        
        

###USING THE CLASS###
bank=Bank()
bank.welcome_note()

option=bank.select_options()


if option == '1':
    bank.create_account()
elif option == '2':
    #account_no=input("Enter the account number : ")
    bank.account_check()
elif option == '3':
    bank.deposit_money()
        
