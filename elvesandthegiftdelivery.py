import math
import queue

#read n, m and k
s = input()

line1 = list(map(int, s.split()))
if len(line1)==2:
    [n,m] = line1
else:
    print('Wrong input, try again')
    
    
Edges = []
for j in range(m):
    s = input()
    line = list(map(int, s.split()))
    [a,b] = line
    a -=1
    b -=1
    Edges.append([a,b])
    
adjacency_matrix = [[0 for i in range(n)] for j in range(n)]

for edge in Edges:
    [a,b] = edge
    adjacency_matrix[a][b] +=1
    adjacency_matrix[b][a] +=1
    

import queue
import math

class Graph: 

    def __init__(self,adjacency_matrix): 
        #adjacency matrix of capacity between vertices
        self.graph = adjacency_matrix

    def BFS(self,source, sink, parents):  
        #create visited set
        Q = queue.Queue()
        visited = set()
        
        #enqueue source
        Q.put(source) 
        visited.add(source)
        
        while (Q.empty()==False): 
            u = Q.get()
            for ind, capacity in enumerate(self.graph[u]): 
                if capacity > 0 and visited.isdisjoint({ind}) : 
                    Q.put(ind)
                    visited.add(ind)
                    parents[ind] = u 
                    if ind == sink:
                        return True
        return visited.isdisjoint({sink})==False
    
    def Ford_Fulkerson(self, source, sink):
        max_flow = 0
        parents = [-1]*n 
        
        while self.BFS(source, sink, parents) : 
            aug_flow = math.inf
            augmenting_path_flow = 0
            u = sink 
            while(u != source): 
                #path flow is minimum edge capacity
                aug_flow = min (aug_flow, self.graph[parents[u]][u]) 
                u = parents[u]
                
            max_flow+=aug_flow
            
            u = sink
            while(u != source):
                self.graph[parents[u]][u] -= aug_flow
                self.graph[u][parents[u]] -= aug_flow
                self.graph[u][parents[u]] += aug_flow 
                u = parents[u]
                
        return max_flow
    
G = Graph(adjacency_matrix)
source = 0
sink = n-1

max_flow = G.Ford_Fulkerson(source, sink)

            
print(str(max_flow) + "\n")
