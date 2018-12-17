#!python3
"""
Путешествующий Дед Мороз.
https://contest.yandex.ru/contest/10360/problems/G/


54.14K:
111 22 47 40 170 89 277 102 259 151 197 107 192 212 11 163 82 193 83 11 28 162 149 208 186 127 226 296 76 181 286 72 73 1 52 265 242 209 242 265 110 17 293 74 122 99 236 229 273 248 285 87 255 25 161 44 166 263 2 156 3 295 225 155 284 292 201 284 201 27 79 43 289 36 33 164 247 153 154 230 154 275 211 98 173 16 91 109 103 51 215 301 241 301 241 301
"""

import heapq
import bisect
import math
import random
import sys

CITY_TIME = 2
MAX_TIME = 372

class G:
    def __init__(self, n):
        self.V = n
        self.city2joy = [0] * n
        self._adj = []
        for i in range(self.V):
            self._adj.append([])
        self.time = {}
        self.names = [None] * n
        self.total_joy = 0

    def add_city(self, inx, name, children, emails):
        EMAIL_JOY = 2
        joy = emails*EMAIL_JOY + (children - emails)
        self.city2joy[inx] = joy
        self.names[inx] = name
        self.total_joy += joy

    def adj(self, v):
        return self._adj[v]

    def add_road(self, v, w, time):
        self._adj[v] += [w]
        self._adj[w] += [v]
        self.time[(v,w)] = time
        self.time[(w,v)] = time


class Tour:
    def __init__(self, cities, graph):
        self.cities = cities.copy()
        self._g = graph
        self._calc_tour()
        assert(self.joy is not None)
        assert(self.time is not None)

    def _calc_tour(self):
        self.marked = [False] * graph.V
        self.joy = 0
        self.time = 0
        cities = self.cities
        g = self._g
        if len(cities) == 0:
            return 0
        joy = g.city2joy[cities[0]]
        time = CITY_TIME
        self.marked[cities[0]] = True
        for i,e in enumerate(cities):
            if i == 0:
                continue
            road_time = g.time[(cities[i-1], e)]
            assert(road_time is not None)
            if time + road_time >= MAX_TIME:
                break
            time += road_time
            if not self.marked[e]:
                if time + CITY_TIME > MAX_TIME:
                    break
                time += CITY_TIME
                joy += g.city2joy[e]
                self.marked[e] = True
        self.joy = joy
        self.time = time

    def print(self):
        print('Tour %d len, %.2fK joy, %d time. Cities:\n%s\n' % (
            len(self.cities),
            self.joy/1000,
            self.time,
            ' '.join(str(c) for c in self.cities)
            ))

    def add_random_cities(self):
        """
        Randomly add cities to left or right of tour till has time.
        """
        g = self._g
        is_left = random.random() >= .5
        v = self.cities[0 if is_left else -1]
        while True:
            adj = g.adj(v)  # adjecent to the city
            tries_num = 3
            w = None
            while tries_num > 0:
                tries_num -= 1
                w = adj[random.randint(0, len(adj)-1)]
                if not self.marked[w]:
                    break
            # add w city:
            w_time = g.time[(v,w)]
            if not self.marked[w]:
                w_time += CITY_TIME
            if self.time + w_time > MAX_TIME:
                break
            if is_left:
                self.cities = [w] + self.cities
            else:
                self.cities = self.cities + [w]
            self.time += w_time
            if not self.marked[w]:
                self.joy += g.city2joy[w]
                self.marked[w] = True
            v = w


class SimulatedAnnealing:
    """
    Метод отжига
    """
    def __init__(self, graph, min_joy, max_joy):
        # choose one with max joy:
        tour = Tour([i for i,e in 
                     enumerate(graph.city2joy) 
                     if e == max(graph.city2joy)], graph)
        max_tour = Tour(tour.cities, graph)
        i_joy = min_joy
        ITER_LIMIT = 100000000000
        for i in range(ITER_LIMIT):
            if i%1000 == 0:
                sys.stdout.write("\r i:%d, limit joy:%.1fK, tour joy:%.1fK, len:%d\n" % 
                                 (i, i_joy/1000, tour.joy/1000, len(tour.cities)))
            # candidate:
            c = self.next_tour(tour, graph)
            if c.joy > tour.joy: 
                tour = c
                if tour.joy > max_tour.joy:
                    max_tour = Tour(tour.cities, graph)
            else:
                delta = c.joy - tour.joy
                p = self.transition_probability(delta, i_joy)
                assert(0<p and p<=1)
                if self.is_transition(p):
                    tour = c
            i_joy = self.increase_joy(min_joy, i)
            if i_joy >= max_joy:
                break
        tour.print()
        self.tour = max_tour

    def increase_joy(self, min_joy, i):
        return min_joy * (.0001*i+1)

    def transition_probability(self, delta, i_joy):
        assert(delta <= 0)
        return math.exp(delta/i_joy)

    def is_transition(self, probability):
        r = random.random()
        return r <= probability;

    def next_tour(self, tour, graph):
        cities = tour.cities.copy()
        num = len(cities)
        assert(num > 0)
        is_at_beginning = random.random() >= .5
        # randomly delete first or last cities in the tour:
        todelete = random.randint(0, 3*num//4)
        if todelete > 0 :
            if is_at_beginning:
                cities = cities[0:todelete]
            else:
                cities = cities[-1:-todelete-1:-1]
        # randomly add cities while has time:
        tour = Tour(cities, graph)
        tour.add_random_cities()
        return tour


if __name__ == '__main__':
    with open('input.txt') as f:
        n = int(f.readline().strip())
        graph = G(n)
        # as cities file has ids not 0-based :
        city_inx = 0
        id_inx = {}
        inx_id = [None] * n
        for i in range(n):
            id,name,childs, emails = f.readline().strip().split(',')
            id = int(id)
            id_inx[id] = city_inx
            inx_id[city_inx] = id
            graph.add_city(city_inx, name, int(childs), int(emails))
            city_inx += 1
        while True:
            l = f.readline()
            if not l:
                break
            edge = [int(i) for i in l.strip().split(',')]
            graph.add_road(id_inx[edge[0]], id_inx[edge[1]], edge[2])

        sa = SimulatedAnnealing(graph, min_joy=3000, max_joy=100000)
        tour = sa.tour
        assert(Tour(tour.cities, graph).joy == tour.joy)
        tour.print()
        print(' '.join(str(inx_id[c]) for c in tour.cities))

        # WEAKER solution using MST:
        # max_tsp = None
        # max_value = 0
        # for ratio in range(1, 11):
        #     ratio = ratio * 0.1
        #     tsp = ApproxTSP(graph, ratio)
        #     if tsp.tour_value > max_value:
        #         max_tsp = tsp
        # print_tour(graph, max_tsp.tour, inx_id)

 
"""
BELOW are weaker solution using minimum spanning tree.
"""

class MinPQ:
    def __init__(self):
        self.arr = []

    def push(self, k, v):
        heapq.heappush(self.arr, (k, v))

    def pop(self):
        return heapq.heappop(self.arr)

    def change_or_push(self, k, v):
        found = False
        for i,e in enumerate(self.arr):
            if e[0] == k:
                self.arr[i] = (k, v)
                found = True
                break
        if found:
            heapq.heapify(self.arr)
        else:
            heapq.heappush(self.arr, (k, v))

    def count(self):
        return len(self.arr)

class ApproxTSP:
    def __init__(self, g, adjusting_ratio):
        self.graph = g
        self.tour = []
        self.tour_value = -1
        self.adjusting_ratio = adjusting_ratio
        for s in range(g.V):
            mst = self.prim(g, s)
            # mst = self.closest_neighbor(g, s)  # weaker than Prim's
            value, tour = self.traverse(mst, g)
            if value > self.tour_value:
                self.tour = tour
                self.tour_value = value

    def closest_neighbor(self, graph, source):
        # find shortest paths:
        INF = 9e9
        distto = [INF] * graph.V
        distto[source] = 0
        pq = MinPQ()
        pq.push(0, source)
        mst = []
        while len(mst) < graph.V and pq.count() > 0:
            v, weight = pq.pop()
            mst += [v]
            # relax:
            for w in graph.adj(v):
                edge_weight = self.get_road_weight(graph, graph.time[(v,w)], v, w)
                if distto[w] > distto[v] + edge_weight:
                    distto[w] = distto[v] + edge_weight
                    pq.change_or_push(w, distto[w])
        return mst

    def prim(self, graph, source):
        minheap = [(0, source)]
        mst = []
        marked = [False] * graph.V
        count = 0
        weight_sum = 0
        while any(minheap) and count < graph.V and weight_sum < MAX_TIME:
            weight, v = heapq.heappop(minheap)
            marked[v] = True
            weight_sum += weight
            mst += [v]
            count += 1
            for w in graph.adj(v):
                if not marked[w]:
                    edge_weight = self.get_road_weight(graph, graph.time[(v,w)], v, w)
                    heapq.heappush(minheap, (edge_weight, w))
        return mst

    def get_road_weight(self, g, road_time, v, w, visited=False):
        weight = road_time + (CITY_TIME if not visited else 0)
        points = sorted(g.city2joy)
        point = g.city2joy[v]
        inx = bisect.bisect_left(points, point)
        # how city is attractable compared to others:
        p = 1 - (inx+1)/g.V  # percentile
        p = p if p > 0 else 0.01
        weight -= (weight * self.adjusting_ratio * p)
        return weight 

    def traverse(self, mst, g):
        time = CITY_TIME
        tour = [mst[0]]
        joy = g.city2joy[mst[0]]
        i = 1
        while time < MAX_TIME and i < len(mst):
            if mst[i] in g.adj(tour[-1]):  # new city
                tour += [mst[i]]
                joy += g.city2joy[mst[i]] if time + CITY_TIME <= MAX_TIME else 0
                time += CITY_TIME + g.time[(tour[-2], tour[-1])]
                i += 1
            else:  # go back
                j = len(tour) - 2
                while mst[i] not in g.adj(tour[-1]) and time < MAX_TIME:
                    tour += [tour[j]]
                    time += g.time[(tour[-2], tour[-1])]
                    j -= 1
        return joy, tour

