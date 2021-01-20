opening_char = ["[","{","("] 
closing_char = ["]","}",")"]

def check_delimiters(input_list):
    opening_stack=[]
    closing_stack=[]
    
    for i in input_list:
        if i in opening_char:
            opening_stack.append(opening_char.index(i))
        elif i in closing_char:
            closing_stack.append(closing_char.index(i))
    
    if sum(opening_stack) == sum(closing_stack):
        return True
    else:
        return False

print(check_delimiters(input()))
