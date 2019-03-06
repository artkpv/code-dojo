#!python3
"""
Bellman-Ford algorithm for finding shortest paths in 
directed graph with negative weights.
"""

POSITIVE_INFINITY = 999

def other(one, sequence):
    """ Returns another item in a sequence """
    assert(len(sequence) == 2)
    return sequence[0] if sequence[1] == one else sequence[1]


class Graph(object):
    """ Simple representation of a graph using adjacency list """
    def __init__(self, verticesnum):
        self.verticesnum = verticesnum
        self.adj = [[] for _ in range(verticesnum)]
        self.weights = {}

    def add(self, start, end, weight):
        self.adj[start] += [end]
        self.weights[(start, end)] = weight


class CycleFinder(object):
    """
    Finds a cycle if any in a directed graph.
    """
    def __init__(self, graph):
        self._graph = graph
        self._marked = [False] * graph.verticesnum
        self._onstack = [False] * graph.verticesnum
        self._edgeto = [None] * graph.verticesnum
        self.cycle = None
        for v in range(graph.verticesnum):
            if not self._marked[v]:
                self._dfs(v)

    def _dfs(self, v):
        self._marked[v] = True
        self._onstack[v] = True
        for w in self._graph.adj[v]:
            if self.cycle:
                return
            elif not self._marked[w]:
                self._edgeto[w] = v
                self._dfs(w)
            elif self._onstack[w]:
                # compose cycle:
                self.cycle = []
                x = v
                while x != w:
                    self.cycle += [x]
                    x = self._edgeto[x]
                self.cycle += [w]
        self._onstack[v] = False


class BellmanFordShortestPaths(object):
    """
    Finds shortest paths to all connected vertices from a
    given source vertex on the graph with negative weights and cycles.
    """
    def __init__(self, graph, source):
        self._graph = graph
        self._source = source
        self._distanceto = [POSITIVE_INFINITY] * graph.verticesnum 
        self._distanceto[self._source] = 0
        self._queue = [self._source]
        self._edgeto = {}
        self._onqueue = set()
        self._onqueue.add(self._source)
        self._cycle = None
        self._cost = 0
        while self._queue and not self.has_negative_cycle():
            self._relax(self._queue.pop(0))

    def _relax(self, v):
        distance = self._distanceto
        graph = self._graph
        for w in graph.adj[v]:
            if distance[w] > distance[v] + graph.weights[(v,w)]:
                distance[w] = distance[v] + graph.weights[(v,w)]
                self._edgeto[w] = (v,w)
                if w not in self._onqueue:
                    self._queue += [w]
                    self._onqueue.add(w)

            # to avoid frequent cycle detection checks:
            if self._cost % self._graph.verticesnum == 0:
                self._find_cycle()

    def _find_cycle(self):
        """ On the shortest paths tree, runs cycles detection """
        tree = Graph(self._graph.verticesnum)
        for key in self._edgeto:
            tree.add(key, other(key, self._edgeto[key]), 0)
        cycleFinder = CycleFinder(tree)
        self._cycle = cycleFinder.cycle

    def has_negative_cycle(self):
        return self._cycle is not None

    def distanceto(self, vertex):
        return self._distanceto[vertex]

    def pathto(self, vertex):
        """
        Shortest path from source to the given vertex. 
        """
        v = vertex
        path = [v]
        while self._source != v:
            edge = self._edgeto[v]
            v = other(v, edge)
            path += [v]
        return list(reversed(path))

    def __repr__(self):
        return ('[\n source=%d,\n distances=%s,\n mst=%s,\n cycle=%s\n]' % 
            (self._source,
             str(self._distanceto),
             str(self._edgeto),
             str(self._cycle)))

"""
#         TESTS         #
"""
def test_4_vertices():
    """
       -.1     
     0 ----> 2
     |       |
     |.1     |.1 
     |       | 
     \/      \/
     1 ----> 3
        .1
    """
    graph = Graph(4)
    graph.add(0, 1, .1)
    graph.add(0, 2, -.1)
    graph.add(1, 3, .1)
    graph.add(2, 3, .1)

    bfsp = BellmanFordShortestPaths(graph, 0)
    assert(bfsp.distanceto(3) == 0)
    assert(bfsp.distanceto(2) == -.1)
    assert(bfsp.distanceto(1) == 0.1)
    assert(bfsp.distanceto(0) == 0)
    assert(bfsp.pathto(3) == [0, 2, 3])

def test_detour():
    """
         3     
     1 ----> 2
     |       |
     |2      | -4
     |       | 
     \/      \/
     4 <---- 3
         2   
    """
    graph = Graph(4)
    graph.add(0, 1, 3)
    graph.add(0, 3, 2)
    graph.add(1, 2, -4)
    graph.add(2, 3, 2)
    bfsp = BellmanFordShortestPaths(graph, 0)
    assert(bfsp.distanceto(3) == 1)
    assert(bfsp.pathto(3) == [0, 1, 2, 3])

def test_negative_cycle_2_vertices():
    """
         1
     1 <---> 2
        -2 
    """
    graph = Graph(2)
    graph.add(0, 1, 1)
    graph.add(1, 0, -2)
    bfsp = BellmanFordShortestPaths(graph, 0)
    # print(bfsp)
    assert(bfsp.has_negative_cycle())

def test_negative_cycle_3_vertices():
    """
         2       2        
     1 ----> 2 <---> 3
                -3       
    """
    graph = Graph(3)
    graph.add(0, 1, 2)
    graph.add(1, 2, 2)
    graph.add(2, 1, -3)
    bfsp = BellmanFordShortestPaths(graph, 0)
    # print(bfsp)
    assert(bfsp.has_negative_cycle())

def test_negative_cycle_5_vertices():
    """
         3         2
     1 ----> 2  <-----> 5
     |       |     -3 
     |2      | -4
     |       | 
     \/      \/
     4 <---- 3
         2   
    """
    graph = Graph(5)
    graph.add(0, 1, 3)
    graph.add(0, 3, 2)
    graph.add(1, 2, -4)
    graph.add(2, 3, 2)
    graph.add(1, 4, 2)
    graph.add(4, 1, -3)
    bfsp = BellmanFordShortestPaths(graph, 0)
    # print(bfsp)
    assert(bfsp.has_negative_cycle())

def test_8_vertices():
    """ Algorithms by Sedgwick & Wayne. p.676 """
    graph = Graph(8)
    graph.add(4, 5, 0.35)
    graph.add(5, 4, 0.35)
    graph.add(4, 7, 0.37)
    graph.add(5, 7, 0.28)
    graph.add(7, 5, 0.28)
    graph.add(5, 1, 0.32)
    graph.add(0, 4, 0.38)
    graph.add(0, 2, 0.26)
    graph.add(7, 3, 0.39)
    graph.add(1, 3, 0.29)
    graph.add(2, 7, 0.34)
    graph.add(6, 2, -1.20)
    graph.add(3, 6, 0.52)
    graph.add(6, 0, -1.40)
    graph.add(6, 4, -1.25)
    bfsp = BellmanFordShortestPaths(graph, 0)
    EPSILON = 0.00001
    assert(bfsp.pathto(6) == [0, 2, 7, 3, 6])
    assert(bfsp.distanceto(6) - 1.51 < EPSILON)
    assert(bfsp.distanceto(7) - .6 < EPSILON)

if __name__ == '__main__':
    test_4_vertices()
    test_detour()
    test_negative_cycle_2_vertices()
    test_negative_cycle_3_vertices()
    test_negative_cycle_5_vertices()
    test_8_vertices()
    print('all tests pass')