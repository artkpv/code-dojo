#!python3
"""
Путешествующий Дед Мороз.
https://contest.yandex.ru/contest/10360/problems/G/

Следующее: определи как в алгоритме Прима определять лучшее расстояние. 
Либо не понятно как вообще тогда считать, ведь мы зависим и от времени и от 
хорошести города (количество детей и писем оттуда)
"""

import heapq

class PrimMST:
   def __init__(self, graph, source):
       minheap = []
       s = [source]
       edgeTo = [None] * graph.V
       INF = 9e9
       distTo = [INF] * graph.V  # how good to get there: time - childs - emails?
       while any(s):
           v = s.pop()
           # relax:
           for w in graph.adj(v):
               pass



def count_tour(g, tour):
    pass

class ApproxTSP:
    def __init__(self, g):
        self.graph = g

        best_tour = []
        best_tour_value = -1
        for s in range(g.V):
            mst = PrimMST(g, s).mst
            tour = traverse_inorder_distinct(mst)
            # assert connected cities:
            for i in range(1, len(tour)):
                v, w = tour[i-1], tour[i]
                assert w in g.adj[v]
            value = count_tour(g, tour)
            if value > best_tour_value:
                best_tour = tour
        self.tour = best_tour


class G:
    def __init__(self, n):
        self.V = n
        self.cities = {}
        self.adj = []
        for i in range(self.V):
            self.adj.append([])
        self.time = {}

    def add_city(self, id, name, children, emails):
        self.cities[id-1] = (name, children, emails)

    def add_road(self, v, w, time):
        v -=1
        w -=1
        self.adj[v] += [w]
        self.time[(v,w)] = time

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
        print(inx_id[i] for i in tsp.tour)

