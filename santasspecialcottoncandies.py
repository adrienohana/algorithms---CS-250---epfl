from collections import defaultdict
import math
import heapq as hq 


entry = input()

first_line = list(map(int, entry.split()))

if len(first_line)!=2:
    print('Error')
else:
    [n,m] = first_line
    
class Graph():

    def __init__(self):
        self.graph = defaultdict(dict)
            
    def add_edge(self, u,v,w):
        self.graph[u-1][v-1]=w
    
    def dijkstra(self):
        dist = [-1]*n
        dist[0] = 0
        
        pqueue = []
        hq.heappush(pqueue, (dist[0], 0))
        hq.heapify(pqueue)
        
        while(pqueue!=[]):
            [_,u] = hq.heappop(pqueue)
            for neighbor in self.graph[u].keys():
                cost = max(dist[u], self.graph[u][neighbor])
                if dist[neighbor]==-1 or cost < dist[neighbor]:
                    dist[neighbor] = cost
                    hq.heappush(pqueue, (dist[neighbor], neighbor))
                    
        print(str(dist[n-1])+"\n")
        return dist[n-1] 
    
G=Graph()
for i in range(m):
    entry = input()
    line = list(map(int, entry.split()))
    [u,v,w]=line
    G.add_edge(u,v,w)
    G.add_edge(v,u,w)
    
G.dijkstra()
