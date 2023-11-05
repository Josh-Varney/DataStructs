class UnGraph:
    def __init__(self):
        self.graph = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
            
    def __str__(self):
        result = ''
        for vertex in self.graph:
            result += f"{vertex} : {self.graph[vertex]}\n"
        return result
            
class DiGraph(UnGraph):
    def __init__(self):
        super().__init__()
    
    def add_edge(self, source, destination):
        if source in self.graph and destination in self.graph:
            self.graph[source].append(destination)
            
if __name__ == '__main__':
    my_digraph = DiGraph()

    my_digraph.add_vertex("A")
    my_digraph.add_vertex("B")
    my_digraph.add_vertex("C")
    
    my_digraph.add_edge("A", "B")
    my_digraph.add_edge("B", "C")
    
    print(my_digraph)

    my_undirected_graph = UnGraph()

    my_undirected_graph.add_vertex("A")
    my_undirected_graph.add_vertex("B")
    my_undirected_graph.add_vertex("C")
    
    my_undirected_graph.add_edge("A", "B")
    my_undirected_graph.add_edge("B", "C")
    
    print(my_undirected_graph)