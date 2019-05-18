# Search methods

import search
# Quiero ir de A a B y la solución esta en search.romania
ab = search.GPSProblem('A', 'B'
                       , search.romania)

print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())
print(search.LowerPath_Cost(ab).path())
print(search.heuristica(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

# Recorrer en Anchura -->
# Recorrer en Profundidad -->
