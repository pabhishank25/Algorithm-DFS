from dfs import Graph

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Depth First Traversal")
g.DFS()
print()
print("*****","ABHISHANK PANDEY","181500011","GLA UNIVERSITY","SECTION-I","CLASS ROLL.NO-02", sep="\n")

