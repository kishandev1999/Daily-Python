#EXERCISE:
'''
PRINT THE HIGH SCORE FROM THE LIST OF STUDENTS MARKS
marks=[96,72,35,94,74,89,91,93]
'''

marks=[96,72,35,94,74,89,99,93]
for i in range(0, len(marks)):
    marks[i] = int(marks[i])
    
highest_score = 0
for score in marks:
    if highest_score < score:
        highest_score = score

print(f"The highest score is  : {highest_score}")