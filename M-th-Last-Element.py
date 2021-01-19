def nthLastElement(n, L):
    res = list(map(int, L.split())) 
    if n <= len(res):
        print(res[-n])
    else:
        print("NIL")

if __name__ == '__main__':
    n = int(input())
    L = str(input())

    nthLastElement(n, L)
