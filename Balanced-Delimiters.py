opening_char = ["[","{","("] 
closing_char = ["]","}",")"]

def check_delimiters(input_list):
    stack = []
    for i in input_list:
        if i in opening_char:
            stack.append(i)
        elif i in closing_char:
            coor = closing_char.index(i)
            if opening_char[coor] == stack[len(stack)-1] and len(stack) != 0:
                stack.pop()
    
    if len(stack) == 0:
        return True
    else:
        return False

print(check_delimiters(input()))
