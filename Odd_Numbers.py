# Complete the 'oddNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def oddNumbers(l, r):
    odds_return = []
    
    for number in range (l,r+1):
        if number %2 ==1:
            odds_return.append(number)
    
    return odds_return
  
if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  l = int(input().strip())

  r = int(input().strip())

  result = oddNumbers(l, r)

  fptr.write('\n'.join(map(str, result)))
  fptr.write('\n')

  fptr.close()
