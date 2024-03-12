'''
TAKE THE STUDENTS HEIGHT IN THE CLASS AND PRINT THE AVERAGE HEIGHT
student_heights=[180,124,165,173,189,169,146]
USE FOR LOOP CONCEPT HERE!
'''

student_heights=[180,124,165,173,189,169,146]
sum_of_heights=0
total_no_of_student=0
for values in student_heights:
    sum_of_heights += values
    total_no_of_student+=1

average_height = sum_of_heights/total_no_of_student
print (f"The average height in the class is : {round(average_height, 2)}")
    

    