#Input:stdin
numbers = input().split(',')

#Initiate result values to 0 (neutral number)
r = 0

#iterate the array and perform a xor operation between each value
#Since the xor of paired values is equal to 0, only the unpaired will be left in result
for number in numbers:
    r = r ^ int(number)

#Output
print(r)
