import random
from art import logo
class CompareBrain():
    def __init__(self,data_list):
        self.score = 0
        self.data_list=data_list
        
    def pop_two_question(self):
        datalist_size=len(self.data_list)
        random_range=random.randint(0,datalist_size)
        statement = self.data_list[random_range]
        print(f"compare A: {statement.name},a {statement.description},from {statement.country}")
        option_A_followers=statement.follower_count      
        self.data_list.remove(statement)
        #print(logo)
        print(f"compare b: {statement.name},a {statement.description},from {statement.country}")
        option_B_followers=statement.follower_count 
        self.compare(option_A_followers,option_B_followers)
    
    '''    
    def compare(self,option_A_followers,option_B_followers):
        if option_A_followers > option_B_followers:
            self.score+=1
        else:
            return
    '''
            
        
        
        
    