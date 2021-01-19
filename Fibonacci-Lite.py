def fibonacci_lite(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci_lite(n-1) + fibonacci_lite(n-2)
    
if __name__ == "__main__":
  n = int(input())
  print(fibonacci_lite(n))
