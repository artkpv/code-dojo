#!python3

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
        n += 1  # wtf ? but cities has it!
        graph = G(n)
        for i in range(n):
            id,name,childs, emails = f.readline().strip().split(',')
            graph.add_city(int(id), name, int(childs), int(emails))
        while True:
            l = f.readline()
            if not l:
                break
            edge = [int(i) for i in l.strip().split(',')]
            graph.add_road(edge[0], edge[1], edge[2])

