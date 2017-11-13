from random import randrange
from itertools import izip_longest
import math

class MinCut(object):
    def __init__(self, graph):
        self.graph = graph
    def findMinCut(self):
        while len(self.graph) > 2:
            indexArr1 = randrange(1, len(self.graph))
            vertexArr1 = self.graph[indexArr1]
            vertex1 = vertexArr1[0]
            vertex2 = vertexArr1[randrange(1, len(vertexArr1))]
            indexArr2 = 0
            for vertexArr in self.graph:
                if vertexArr[0] == vertex2:
                    vertexArr2 = vertexArr
                    break
                indexArr2 += 1
            self.graph[indexArr1] = [a for a in vertexArr1 if a != vertex2]
            vertexArr2 = [b for b in vertexArr2 if b != vertex1]
            # for elem1, elem2 in izip_longest(vertexArr1, vertexArr2):
            #     if elem1 == vertex2:
            #         vertexArr1.remove(elem1)
            #     if elem2 == vertex1:
            #         vertexArr2.remove(elem2)
            self.graph[indexArr1].extend(vertexArr2[1:])
            del self.graph[indexArr2]
            i = 0
            for arr in self.graph:
                self.graph[i] = [vertex1 if vertex==vertex2 else vertex for vertex in arr]
                i += 1
        return len(self.graph[0]) - 1

            # for vertexArr in self.graph:
            #     if vertex2 in vertexArr[0]:
            #         vertexArr2 = vertexArr
            #         break
            # print vertex1
            # print vertexArr1
            # print vertex2
            # print vertexArr2
            # for elem1, elem2 in izip_longest(vertexArr1, vertexArr2):
            #     if elem1 == vertex2:
            #         vertexArr1.remove(elem1)
            #     if elem2 in vertex1:
            #         vertexArr2.remove(elem2)
            # print vertex1
            # print vertexArr1
            # print vertex2
            # print vertexArr2
            # a = [1,2,3]
            # for n in a:
            #     a[n] = 5
            # print a
            # return

minimumCut = 0

# file = open('kargerMinCut.txt', "r")
# graph = file.read().split('\r\n')
# i = 0
# while i < len(graph):
#     adj_vertices = graph[i].split('\t')
#     vertex = map(int, adj_vertices)
#     graph[i] = vertex
#     i += 1

# graph = [[[1], 2, 3, 4], [[2], 3, 1], [[3], 4, 2, 1], [[4], 1, 3]]
graph = [[1, 2, 3, 4], [2, 3, 1], [3, 4, 2, 1], [4, 1, 3]]

nodes = len(graph)

numberOfTrials = int(nodes ** 2 * math.log(nodes))
print numberOfTrials

minCut = MinCut(graph)

for x in range(numberOfTrials):
    cut = minCut.findMinCut()
    if minimumCut == 0 or cut < minimumCut:
        minimumCut = cut
    print minimumCut

# print minimumCut
