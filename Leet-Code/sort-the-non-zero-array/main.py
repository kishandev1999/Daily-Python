list1=[1, 0,2,0,3,53,5]
#Output list1=[1,2, 3,53,5,0,0]

class Sorting():
    def __init__(self,input):
        self.input = input
        
    def separating_method(self):
        collect_zero=[]
        non_zero=[]
        for i in self.input:
            if i == 0:
                collect_zero.append(i)
            else:
                non_zero.append(i)
        

        non_zero.sort()
        print(non_zero+collect_zero)
        #final_list=sorted_arry+collect_zero
        #print(final_list)


sort = Sorting(list1)
sort.separating_method()


                
                
        
                
        
    