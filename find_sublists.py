'''
find all possible sublists of a list, collecting into a new list of lists
'''
from itertools import combinations
def sub_lists(input_list):
	subs = []
	for i in range(0, len(input_list)+1):
	  temp = [list(x) for x in combinations(input_list, i)]
	  if len(temp)!=0:
	    subs.extend(temp)
   
	return subs

l1 = [10, 20, 30, 40]
print(sub_lists(l1))
#output:[[], [10], [20], [30], [40], [10, 20], [10, 30], [10, 40], [20, 30], [20, 40], [30, 40], 
#		[10, 20, 30], [10, 20, 40], [10, 30, 40], [20, 30, 40], [10, 20, 30, 40]]
