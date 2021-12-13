

class Vertex:
    def __init__(self, vertex):
        self.name = vertex
        self.neighbors = []
        
    def add_neighbor(self, neighbor):
        if isinstance(neighbor, Vertex):
            if neighbor.name not in self.neighbors:
                self.neighbors.append(neighbor.name)
                neighbor.neighbors.append(self.name)
                self.neighbors = sorted(self.neighbors)
                neighbor.neighbors = sorted(neighbor.neighbors)
        else:
            return False
        
    def add_neighbors(self, neighbors):
        for neighbor in neighbors:
            if isinstance(neighbor, Vertex):
                if neighbor.name not in self.neighbors:
                    self.neighbors.append(neighbor.name)
                    neighbor.neighbors.append(self.name)
                    self.neighbors = sorted(self.neighbors)
                    neighbor.neighbors = sorted(neighbor.neighbors)
            else:
                return False
        
    def __repr__(self):
        return str(self.neighbors)

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex):
            self.vertices[vertex.name] = vertex.neighbors

            
    def add_vertices(self, vertices):
        for vertex in vertices:
            if isinstance(vertex, Vertex):
                self.vertices[vertex.name] = vertex.neighbors
            
    def add_edge(self, vertex_from, vertex_to):
        if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
            vertex_from.add_neighbor(vertex_to)
            if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
                self.vertices[vertex_from.name] = vertex_from.neighbors
                self.vertices[vertex_to.name] = vertex_to.neighbors
                
    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0],edge[1])          
    
    def adjacencyList(self):
        if len(self.vertices) >= 1:
                return [str(key) + ":" + str(self.vertices[key]) for key in self.vertices.keys()]  
        else:
            return dict()
        
    def adjacencyMatrix(self):
        if len(self.vertices) >= 1:
            self.vertex_names = sorted(g.vertices.keys())
            self.vertex_indices = dict(zip(self.vertex_names, range(len(self.vertex_names)))) 
            import numpy as np
            self.adjacency_matrix = np.zeros(shape=(len(self.vertices),len(self.vertices)))
            for i in range(len(self.vertex_names)):
                for j in range(i, len(self.vertices)):
                    for el in g.vertices[self.vertex_names[i]]:
                        j = g.vertex_indices[el]
                        self.adjacency_matrix[i,j] = 1
            return self.adjacency_matrix
        else:
            return dict()              
                        
def graph(g):
    """ Function to print a graph as adjacency list and adjacency matrix. """
    return str(g.adjacencyList())
    #return str(g.adjacencyList()) + '\n' + '\n' + str(g.adjacencyMatrix())

###################################################################################

#g is the graph
#s is the starting vertex
#e is the ending vertex
#visited is the list of visited vertices
#path is the path currently taken
def findAllPaths(g, s, e, path):
    #print('state: ', s, path)
    #are we at the ending vertex?
    if s == e:
        return 1
    #is this the second time visiting a lowercase node?
    if s.islower() and s in path:
        return 0
    #continue searching, adding this node to the list
    ans = 0
    #print('visible vertices: ', g.vertices[s])
    for a in g.vertices[s]:
        tmp = path.copy()
        tmp.append(s)
        #continue along all neighboring nodes
        ans += findAllPaths(g, a, e, tmp)
    return ans

#second finding function
#usedLittle is False if you haven't visited a small not 2x yet, True otherwise
def findAllPaths2(g, s, e, path, usedLittle):
    #print('state: ', s, path)
    #are we at the ending vertex?
    if s == e:
        return 1
    #is this the second time visiting a lowercase node?
    if s.islower() and s in path:
        if usedLittle or s == 'start' or s == 'end':
            return 0
        else:
            usedLittle = True
    #continue searching, adding this node to the list
    ans = 0
    #print('visible vertices: ', g.vertices[s])
    for a in g.vertices[s]:
        tmp = path.copy()
        tmp.append(s)
        #continue along all neighboring nodes
        ans += findAllPaths2(g, a, e, tmp, usedLittle)
    return ans


    
if __name__ == '__main__':
    #format the input
    fd = open('input.txt')
    inputs = fd.readlines()
    fd.close

    fd = open('input.txt')
    tst = fd.readlines()
    fd.close

    #format inputs
    for i, a in enumerate(tst):
        li = []
        a = a.strip()
        a = a.split('-')
        for b in a:
            li.append(b)
        tst[i] = li

    for i, a in enumerate(inputs):
        li = []
        a = a.strip()
        for b in a:
            li.append(b)
        inputs[i] = li

    #construct a list of all the vertices
    tstPts = []
    tstVert = []
    for a in tst:
        for b in a:
            if b not in tstPts:
                tstPts.append(b)
                tstVert.append(Vertex(b))
    #have a list of unique nodes

    #add the edges
    for a in tst:
        x = a[0]
        y = a[1]
        tstVert[tstPts.index(x)].add_neighbor(tstVert[tstPts.index(y)])
    tstg = Graph()
    for a in tstVert:
        tstg.add_vertex(a)

    #print the completed graph
    #print(graph(tstg))

    #print(tstg.vertices['start'])
    #print(findAllPaths(tstg, 'start', 'end', list()))
    print(findAllPaths2(tstg, 'start', 'end', list(), False))
    
    #printing stuff
    #print(tst)
    #print(tstPts)
    #print(tstVert)
    #print(tstMapping)


    
