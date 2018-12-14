#!python3
"""
Путешествующий Дед Мороз.
https://contest.yandex.ru/contest/10360/problems/G/

Следующее: Попробовать на основе алгоримта для кратчайших путей, а не минимального оставного дерева.

"""

import heapq
import bisect


class ApproxTSP:
    def __init__(self, g, max_time, adjusting_ratio):
        self.graph = g
        self.max_time = max_time
        self.tour = []
        self.tour_value = -1
        self.adjusting_ratio = adjusting_ratio
        for s in range(g.V):
            mst = self.prim(g, s)
            value, tour = self.traverse(mst, g)
            if value > self.tour_value:
                self.tour = tour
                self.tour_value = value

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
                    edge_weight = self.get_road_weight(graph, graph.time[(v,w)], v, w, marked)
                    heapq.heappush(minheap, (edge_weight, w))
        return mst

    def get_road_weight(self, g, road_time, v, w, visited):
        weight = road_time + (2 if w not in visited else 0)
        return weight
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
        happyness = g.cities[mst[0]][1]
        i = 1
        while time < self.max_time and i < len(mst):
            if mst[i] in g.adj(tour[-1]):  # new city
                tour += [mst[i]]
                happyness += g.cities[mst[i]][1] if time + 2 <= self.max_time else 0
                time += 2 + g.time[(tour[-2], tour[-1])]
                i += 1
            else:  # go back
                j = len(tour) - 2
                while mst[i] not in g.adj(tour[-1]) and time < self.max_time:
                    tour += [tour[j]]
                    time += g.time[(tour[-2], tour[-1])]
                    j -= 1
        return happyness, tour


class G:
    def __init__(self, n):
        self.V = n
        self.cities = {}
        self._adj = []
        for i in range(self.V):
            self._adj.append([])
        self.time = {}
        self.total_happyness = 0
        self._city_points = []

    def add_city(self, inx, name, children, emails):
        happyness = emails*2 + (children - emails)
        self.cities[inx] = (name, happyness)
        self._city_points += [happyness]
        self._city_points = sorted(self._city_points)
        self.total_happyness += happyness

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
    happyness = g.cities[tour[0]][1]
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
            happyness += g.cities[e][1]
            marked[e] = True
    print('Tour len:', len(tour))
    print('Happyness:', happyness)


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

        max_tsp = None
        max_value = 0
        for ratio in range(1, 11):
            ratio = ratio * 0.1
            tsp = ApproxTSP(graph, max_time, ratio)
            if tsp.tour_value > max_value:
                max_tsp = tsp
        print_tour(graph, max_tsp.tour, max_time, inx_id)

