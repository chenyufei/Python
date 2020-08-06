class GraphSearch:
    def __init__(self, graph):
        self.graph = graph

    def find_path(self, start, end, path=None):
        self.start = start
        self.end = end
        if not path:
            self.path = []
        self.path.extend([self.start])
        if self.start not in self.graph:
            return None  # 如果图里面没有这个start这个key,说明这条路不同,返回None
        if self.start == self.end:
            return self.path

        for node in self.graph[self.start]:
            if node not in self.path:
                newpath = self.find_path(node, self.end, self.path)
                if newpath:  # newpath不存在的时候说明这条路没有走通,继续循环,走下一条路
                    return newpath
        return None  # 如果上面一直没有return,走到这里说明从start没有找到end.返回None

    # def find_all_path(self, start, end, path=None, run_num=[]):
    #     self.start = start
    #     self.end = end
    #     if not path:
    #         self.path = []
    #     self.path.extend([self.start])
    #     paths = []
    #     if self.start not in self.graph:
    #         return []
    #     if self.start == self.end:
    #         if len(run_num) == 0:
    #             paths.append([self.start])
    #         else:
    #             return [self.path]
    #     for node in self.graph[self.start]:
    #         if node not in self.path:
    #             run_num.append(1)
    #             newpaths = self.find_all_path(node, self.end, self.path)
    #             for newpath in newpaths:
    #                 paths.append(newpath)
    #     return paths
    def find_all_path(self, start, end, path=None):
        self.start = start
        self.end = end
        if not path:
            self.path = []
        self.path += [self.start]
        if self.start == self.end:
            return [self.path]
        if self.start not in self.graph:
            return []
        paths = []
        for node in self.graph[self.start]:
            if node not in self.path:

                newpaths = self.find_all_path(node, self.end, self.path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


    def find_shortest_path(self, start, end, path=None):
        self.start = start
        self.end = end
        if not path:
            self.path = []
        self.path.extend(self.start)
        if self.start not in self.graph:
            return None
        if self.start == self.end:
            return self.path

        shortpath = None
        for node in self.graph[self.start]:
            if node not in self.path:
                newpath = self.find_shortest_path(node, self.end, self.path)
                if newpath:
                    if not shortpath or len(newpath) < len(shortpath):
                        shortpath = newpath
        return shortpath


graph = {
    "A": ["B", "C"],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['A'],
    'E': ['F'],
    'F': ['C']
}

graph1 = GraphSearch(graph)
print(graph1.find_path("A", "D"))
print(graph1.find_all_path("A", "A"))
print(graph1.find_all_path("A", "D"))
print(graph1.find_shortest_path("A", "D"))
