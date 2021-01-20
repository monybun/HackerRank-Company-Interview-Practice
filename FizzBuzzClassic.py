def fizzBuzz(n):
    for i in range(n+1):
        if i == 0: continue
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            continue
        elif i % 3 == 0:
            print("Fizz")
            continue
        elif i % 5 == 0:
            print("Buzz")
            continue
        print(i)

n = int(input().strip())

fizzBuzz(n)
