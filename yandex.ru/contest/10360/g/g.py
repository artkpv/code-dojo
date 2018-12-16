#!python3
"""
Путешествующий Дед Мороз.
https://contest.yandex.ru/contest/10360/problems/G/

"""

import heapq
import bisect
import math
import random

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
    def __init__(self, g, max_time, adjusting_ratio):
        self.graph = g
        self.max_time = max_time
        self.tour = []
        self.tour_value = -1
        self.adjusting_ratio = adjusting_ratio
        for s in range(g.V):
            # mst = self.prim(g, s)
            mst = self.closest_neighbor(g, s)
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
        while any(minheap) and count < graph.V and weight_sum < self.max_time:
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
        weight = road_time + (2 if not visited else 0)
        points = g.get_city_points()
        point = g.cities[v][1]
        inx = bisect.bisect_left(points, point)
        # how city is attractable compared to others:
        p = 1 - (inx+1)/g.V  # percentile
        p = p if p > 0 else 0.01
        weight -= (weight * self.adjusting_ratio * p)
        return weight 
 

    def traverse(self, mst, g):
        time = 2
        # marked = [False] * g.V
        # marked[mst[0]] = True
        tour = [mst[0]]
        joy = g.cities[mst[0]][1]
        i = 1
        while time < self.max_time and i < len(mst):
            if mst[i] in g.adj(tour[-1]):  # new city
                tour += [mst[i]]
                joy += g.cities[mst[i]][1] if time + 2 <= self.max_time else 0
                time += 2 + g.time[(tour[-2], tour[-1])]
                i += 1
            else:  # go back
                j = len(tour) - 2
                while mst[i] not in g.adj(tour[-1]) and time < self.max_time:
                    tour += [tour[j]]
                    time += g.time[(tour[-2], tour[-1])]
                    j -= 1
        return joy, tour


class G:
    def __init__(self, n):
        self.V = n
        self.cities = {}
        self._adj = []
        for i in range(self.V):
            self._adj.append([])
        self.time = {}
        self.total_joy = 0
        self._city_points = []

    def add_city(self, inx, name, children, emails):
        joy = emails*2 + (children - emails)
        self.cities[inx] = (name, joy)
        self._city_points += [joy]
        self._city_points = sorted(self._city_points)
        self.total_joy += joy

    def get_city_points(self):
        # return sorted asc city weights
        return self._city_points

    def adj(self, v):
        return self._adj[v]

    def add_road(self, v, w, time):
        self._adj[v] += [w]
        self._adj[w] += [v]
        self.time[(v,w)] = time
        self.time[(w,v)] = time

def print_tour(g, tour, max_time, inx_id):
    print('Tour:')
    print(' '.join(str(inx_id[i]) for i in tour))
    assert(len(tour) > 0)
    joy = g.cities[tour[0]][1]
    city_time = 2
    time = city_time
    marked = [False] * g.V
    marked[tour[0]] = True
    for i,e in enumerate(tour):
        if i == 0:
            continue
        time += g.time[(tour[i-1], e)]
        if time >= max_time:
            break
        if not marked[e]:
            if time + city_time > max_time:
                break
            time += city_time
            joy += g.cities[e][1]
            marked[e] = True
    print('Tour len:', len(tour))
    print('joy:', joy)

class Tour:
    def __init__(self, cities, graph, max_time):
        self.cities = cities
        self._g = graph
        self._max_time = max_time
        self._calc_joy()
        assert(self.joy is not None)
        assert(self.time is not None)

    def print(self):
        print(self.cities)

    def _calc_joy(self):
        cities = self.cities
        g = self._g
        max_time = self._max_time
        if len(cities) == 0:
            return 0
        joy = g.cities[cities[0]][1]
        city_time = 2
        time = city_time
        marked = [False] * g.V
        marked[cities[0]] = True
        for i,e in enumerate(cities):
            if i == 0:
                continue
            road_time = g.time[(cities[i-1], e)]
            if time + road_time >= max_time:
                break
            time += road_time
            if not marked[e]:
                if time + city_time > max_time:
                    break
                time += city_time
                joy += g.cities[e][1]
                marked[e] = True
        self.joy = joy
        self.time = time

class SimulatedAnnealing:
    def __init__(self, graph, max_time, min_joy, max_joy):
        # choose one with max joy:
        tour = Tour([i for i,e in 
                     enumerate(graph.cities) 
                     if e[1] == graph.get_city_points()[-1]], graph, max_time)
        current_joy = tour.joy
        limit_joy = min_joy
        for i in range(100000):
            candidate = self.next_tour(tour, graph, max_time)
            c_joy = tour.joy
            if c_joy < current_joy: 
                current_joy = c_joy
                tour = candidate
            else:
                p = self.transition_probability(c_joy - current_joy, limit_joy)
                if self.is_transition(p):
                    current_joy = c_joy
                    tour = candidate
            limit_joy = self.increase_joy(min_joy, i)
            if limit_joy >= max_joy:
                break
        self.tour = tour

    def increase_joy(self, min_joy, i):
        return min_joy * (1 + 0.1 * i)

    def transition_probability(self, dE, e):
        return math.exp(-dE,e)

    def is_transition(self, probability):
        r = random.random()
        return r <= probability;

    def next_tour(self, tour, graph, max_time):
        # randomly modify tour but keep it within max time
        cities = tour.cities
        num = len(cities)
        assert(num > 0)
        # delete some:
        todelete = random.randint(0, num//2)
        if todelete > 0 :
            deleted = [False] * graph.V
            even = True
            i = 0
            def delete_one_city():
                pass
            while todelete > 0:
                v = cities[i]
                if not deleted[v]:
                    is_leaf = i == 0 or i == num - 1
                    if i % 2 == 0 and even:
                        pass # delete
                    else:
                        pass
               i = (i+1) % num


if __name__ == '__main__':
    with open('cities') as f:
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
        max_time = 372

        max_joy = 47000
        sa = SimulatedAnnealing(graph, max_time, max_joy)
        tour = sa.tour
        print(tour.print())
        print(tour.joy)

        # max_tsp = None
        # max_value = 0
        # for ratio in range(1, 11):
        #     ratio = ratio * 0.1
        #     tsp = ApproxTSP(graph, max_time, ratio)
        #     if tsp.tour_value > max_value:
        #         max_tsp = tsp
        # print_tour(graph, max_tsp.tour, max_time, inx_id)

