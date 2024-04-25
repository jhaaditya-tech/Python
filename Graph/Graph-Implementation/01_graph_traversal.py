from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list={}
        
    #Adding vertex    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
           self.adjacency_list[vertex]=[]
           return True
        return False 
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])
        
    #Adding edge to the graph
    def add_edge(self, vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    #Removing edge method
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    
    #Removing vertex from graph, should remove edge as well
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False
    
    #Breadth First Search
    def bfs(self, vertex):
        visited=set()
        visited.add(vertex)
        queue=deque(vertex)
        while queue:
            current_vertex=queue.popleft()
            print(current_vertex)
            for adjacenet_vertex in self.adjacency_list[current_vertex]:
                if adjacenet_vertex not in visited:
                    visited.add(adjacenet_vertex)
                    queue.append(adjacenet_vertex)

    #Depth First Search
    def dfs(self, vertex):
        visited=set()
        stack=[vertex]
        while stack:
            current_vertex=stack.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    stack.append(adjacent_vertex)
        
        
        
    

        
   




custom_graph=Graph()
custom_graph.add_vertex("A")
custom_graph.add_vertex("B")
custom_graph.add_vertex("C")
custom_graph.add_vertex("D")
custom_graph.add_vertex("E")
custom_graph.add_edge("A","B")
custom_graph.add_edge("A","C")
custom_graph.add_edge("B","E")
custom_graph.add_edge("C","D")
custom_graph.add_edge("D","E")


custom_graph.print_graph()
custom_graph.bfs("A")
custom_graph.dfs("A")


        
        