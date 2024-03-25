import math
def paint_cal(height, width, cover):
    num_of_cans = (height * width) /cover
    round_up_cans=math.ceil(num_of_cans)
    print(f"You'll need {round_up_cans} cans to paint")
    
paint_cal(4,5,5)