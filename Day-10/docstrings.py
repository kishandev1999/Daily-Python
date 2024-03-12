#DOC STRINGS ARE NOTHING BUT DOCUMENTING WITH MULTIPLE STINGS OR LINES
#EXAMPLE:
def format_function2(f_name,l_name):
    if f_name == "" or l_name == "" :
        #return
        #BY DEFAULT THIS RETURN WILL BE "none"
        return "You haven't provided any inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    #the below way of writing documentation for the code is called as DOCSTRING
    '''
    HERE WE ARE FORMATTING THE FIRST NAME AND LAST NAME
    AND WE ARE USING A BUILT IN FUNCTION CALL .title()
    '''
    return f"{formatted_f_name} {formatted_l_name}"