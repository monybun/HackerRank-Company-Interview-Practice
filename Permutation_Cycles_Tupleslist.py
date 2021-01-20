def to_cycles(perm):
    pi = {i+1: perm[i] for i in range(len(perm))}
    cycles = []

    while pi:
        elem0 = next(iter(pi)) # arbitrary starting element
        this_elem = pi[elem0]
        next_item = pi[this_elem]

        cycle = []
        while True:
            cycle.append(this_elem)
            del pi[this_elem]
            this_elem = next_item
            if next_item in pi:
                next_item = pi[next_item]
            else:
                break
        a = ' '.join(map(str, tuple(cycle)))
        b = '('+a+')'
        cycles.append(b)
       
    return cycles


print(to_cycles([1]))
# ['(1)']

print(to_cycles([4,1,6,2,3,5]))
# ['(4 2 1)', '(6 5 3)']
