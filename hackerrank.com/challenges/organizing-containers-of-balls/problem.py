#!python3

q = int(input())

def is_possible(types, capacity):
    s_capacity = sorted(capacity)
    s_types = sorted(types)

    for i in range(n):
        if s_capacity[i] != s_types[i]:
            return False
    return True

for q_itr in range(q):
    n = int(input())

    container = []
    capacity = [0] * n
    types = [0] * n

    for i in range(n):
        types_in_container = list(map(int, input().rstrip().split()))
        container.append(types_in_container)
        capacity[i] = sum(types_in_container)
        for t in range(n):
            types[t] += types_in_container[t]

    result = is_possible(types, capacity)

    print('Possible' if result else 'Impossible')
