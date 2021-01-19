import sys
cache = {}

def fibonacci_return(n):
    '''Return a fibonacci sequence value of num'''

    if n in cache:
        return cache[n]

    if n == 0:
        result = 0
    elif n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci_cache(n - 2) + fibonacci_cache(n - 1)

    cache[n] = result
    return result

for i in sys.stdin:
    print(fibonacci_return(int(i)))
