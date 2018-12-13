#!python3
"""
Путешествующий Дед Мороз.
https://contest.yandex.ru/contest/10360/problems/G/

Следующее: определи как в алгоритме Прима определять лучшее расстояние. 
Либо не понятно как вообще тогда считать, ведь мы зависим и от времени и от 
хорошести города (количество детей и писем оттуда)
"""

import heapq


class ApproxTSP:
    def __init__(self, g):
        self.graph = g
        self.max_time = 372
        self.best_tour = []
        self.best_tour_value = -1
        for s in range(g.V):
            print('From source', s)
            mst = self.prim(g, s)
            # print(' mst:', str(mst))
            value, tour = self.traverse(mst, g)
            print(' value:', value, 'len tour:', len(tour))
            if value > self.best_tour_value:
                self.best_tour = tour
                self.best_tour_value = value

    def prim(self, graph, source):
        minheap = [(0, source)]
        mst = []
        marked = [False] * graph.V
        count = 0
        weight_sum = 0
        while any(minheap) and count < graph.V and weight_sum < self.max_time:
            weight, v = heapq.heappop(minheap)
            if marked[v]:  # HACK . TODO
                continue
            marked[v] = True
            weight_sum += 2
            mst += [v]
            count += 1
            for w in graph.adj(v):
                if not marked[w]:
                    edge_weight = graph.time[(v,w)]
                    heapq.heappush(minheap, (edge_weight, w))
        return mst

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

    def add_city(self, inx, name, children, emails):
        happyness = emails*2 + (children - emails)
        self.cities[inx] = (name, happyness)

    def adj(self, v):
        return self._adj[v]

    def add_road(self, v, w, time):
        self._adj[v] += [w]
        self._adj[w] += [v]
        self.time[(v,w)] = time
        self.time[(w,v)] = time

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
        tsp = ApproxTSP(graph)
        print(tsp.best_tour_value)
        print(tsp.best_tour)

