def fibonacci_lite(n):
    if n == 0 or n == 1:
        return n
    
    return fibonacci_lite(n-1) + fibonacci_lite(n-2)
    
if __name__ == "__main__":
  n = int(input())
  print(fibonacci_lite(n))
