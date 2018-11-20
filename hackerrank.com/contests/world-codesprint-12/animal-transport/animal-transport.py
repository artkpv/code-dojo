#!python3
import sys, itertools

class Animal:
    def __init__(self, from_, type_, to):
        self.from_ = from_
        self.type_ = type_
        self.to = to

    def __repr__(self):
        return '{} {} {}'.format(self.from_, self.type_, self.to)

def get_animals_we_can_take(in_zoo, taken, animals):
    table = {'D': 'E', 'C': 'D', 'M': 'C', 'E': 'M'}
    can_not_take = set(table[t] for t in set(animals[i].type_ for i in taken))
    return [i for i in in_zoo if animals[i].type_ not in can_not_take ]

def visit_zoo(zoo_num, taken, to_deliver_num, zoos, animals, zoos_num, D=None):
    """
    in  : taken [(destination, type)] * num
          zoo inx
          to deliver num
    out : min zoo reached
    """
    #sys.stdout.write(' ({} {} {}) '.format(zoo_num, taken, to_deliver_num))
    if zoo_num > zoos_num:
        #sys.stdout.write('\n')
        return None  # didn't deliver the required number of matching animals
    unloaded = 0
    for i in taken:
        if animals[i].to == zoo_num:
            taken.remove(i)
            unloaded += 1
    if unloaded >= to_deliver_num:  # Finished
        #sys.stdout.write(' Found ' + str(zoo_num) + "\n")
        return zoo_num

    # need to deliver more:
    if zoo_num in zoos:  # this zoo has animals
        can_take = get_animals_we_can_take(zoos[zoo_num], taken, animals)
        min_zoo_found = None
        for y in range(0, 2**len(can_take)):  # taking 0 or some
            taken_new = []
            shift = 0
            while (y >> shift) > 0:
                if (y >> shift) & 1 == 1:
                    taken_new += [can_take[shift]]
                shift += 1

            min_zoo_for_this_comb = visit_zoo(
                zoo_num + 1,
                taken + taken_new,
                to_deliver_num - unloaded,
                zoos,
                animals,
                zoos_num,
                D)
            if min_zoo_found == None or min_zoo_found > min_zoo_for_this_comb:  # this combination was closer
                min_zoo_found = min_zoo_for_this_comb
        return min_zoo_found
    else:  # this zoo doesn't have animals
        return visit_zoo(zoo_num + 1, taken, to_deliver_num - unloaded, zoos, animals, zoos_num, D)


def minimumZooNumbers(zoos_num, animals_num, types, sources, destinations):
    # Return a list of length n consisting of the answers
    animals = (Animal(sources[i], types[i], destinations[i]) for i in range(animals_num))
    # w/o those who already in their zoos!
    animals = [a for a in animals if a.from_ < a.to]  # can not deliver back
    # get animals by zoo:
    animals_by_zoos = {}  # indexes of animals by zoo_num
    for i in range(len(animals)):
        a = animals[i]
        zoo_num = a.from_
        if zoo_num not in animals_by_zoos:
            animals_by_zoos[zoo_num] = []
        animals_by_zoos[zoo_num].append(i)

    first_zoo_num = 1
    res = []
    #print(animals)
    #print(animals_by_zoos)
    for to_deliver_num in range(1, animals_num + 1):
        min_zoo_reached = visit_zoo(first_zoo_num, list(), to_deliver_num, animals_by_zoos, animals, zoos_num)
        res += [min_zoo_reached or -1]
        # print("To deliver ", to_deliver_num, ", ", min_zoo_reached, " zoo reached")
    return res


if __name__ == "__main__":
    cases = int(input().strip())
    for a0 in range(cases):
        m, n = input().strip().split(' ')
        m, n = [int(m), int(n)]
        t = input().strip().split(' ')
        s = list(map(int, input().strip().split(' ')))
        d = list(map(int, input().strip().split(' ')))
        result = minimumZooNumbers(m, n, t, s, d)
        print (" ".join(map(str, result)))


