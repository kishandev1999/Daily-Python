#GRADING THE STUDENTS AS PER THEIR MARKS
'''
SCORE 91-100      : GRADE - OUTSTANDING
SCORE 81-90       : GRADE - EXCEEDS EXPECTATIONS
SCORE 71-80       : GRADE - ACCEPTABLE
SCORE 70 OR LOWER : GRADE - FAIL
'''
student_scores={
    "Harry" : 81,
    "Kishan":99,
    "Manas":97,
    "Arun":34,
    "Datta":64
}

#create a empty dictionary called student grade
student_grade={}

for key in student_scores:
    if student_scores[key] > 90:
        student_grade[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grade[key] = "EXCEEDED EXPECTATIONS"
    elif student_scores[key] > 70:
        student_grade[key] = "ACCEPTABLE"
    else:
        student_grade[key] = "FAIL"
        
print(student_grade)