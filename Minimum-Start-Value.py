
def MinStart(arr):
    start_flag = 0
    while True:
        rolling_sum = start_flag
        for i in arr:
            rolling_sum += i
            if rolling_sum < 1:
                break
        if rolling_sum >= 1:
            return start_flag
        start_flag += 1


print(MinStart([-2, 3, 1, -5])) 
#output 4
print(MinStart([-5, 4, -2, 3, 1]))  
#output 6
print(MinStart([-5, 4, -2, 3, 1, -1, -6, -1, 0, -5]))  
#output 13
print(MinStart([-5, 4, -2, 3, 1, -1, -6, -1, 0, 5]))  
#output 8
