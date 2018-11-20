"""
 c = 16
 n = 100

 offices  = 1600
 queries = 1000
 q_cities = 16000

"""

def _query(querycities, cities):
    """
    Moscow
      001
      101
      or = 101
    SPb
      010
      100
      or = 110
    and = 100

    """
    cities = [c for c in cities if c[0] in querycities]
    result = []
    if len(cities) == 0:
        return result
    andCities = cities[0][1][0]  # orOfficies
    for city in cities[1:]:
        andCities &= city[1][0]
        # print('city[1][0] =', city[1][0])
        # print('andCities=', andCities)
        if andCities == 0:  # no available
            return result
    for c in cities:
        for o in c[1][1]:  # officies
            if o[1] & andCities != 0:  # in this office we have free hours
                result += [o[0]]
                break
    return result


c = int(input().strip())
cities = []
for i in range(c):
    city, n = input().strip().split(' ')
    offices = []
    officesOr = 0
    for j in range(int(n)):
        hours, name = input().strip().split(' ')
        available = int(''.join('1' if h == '.' else '0' for h in hours), 2)
        offices += [(name, available)]
        officesOr |= available

    cities += [(city, (officesOr, offices))]

# print(cities)

m = int(input().strip())
for i in range(m):
    query = input().strip().split(' ')[1:]
    r = _query(query, cities)
    print('Yes ' + ' '.join(r) if len(r) > 0 else 'No')






