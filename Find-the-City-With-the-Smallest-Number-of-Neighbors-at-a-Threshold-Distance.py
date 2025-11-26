1from typing import List
2
3class Solution:
4    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
5        # Initialize the distance matrix with infinity
6        dist = [[float('inf')] * n for _ in range(n)]
7        
8        # Distance to itself is 0
9        for i in range(n):
10            dist[i][i] = 0
11        
12        # Populate the distance matrix with the given edges
13        for u, v, w in edges:
14            dist[u][v] = w
15            dist[v][u] = w
16        
17        # Floyd-Warshall algorithm
18        for k in range(n):
19            for i in range(n):
20                for j in range(n):
21                    if dist[i][j] > dist[i][k] + dist[k][j]:
22                        dist[i][j] = dist[i][k] + dist[k][j]
23        
24        # Find the city with the smallest number of reachable cities
25        # and if there is a tie, choose the city with the greatest number.
26        minReachableCities = float('inf')
27        bestCity = -1
28        
29        for i in range(n):
30            reachableCities = 0
31            for j in range(n):
32                if dist[i][j] <= distanceThreshold:
33                    reachableCities += 1
34            
35            if reachableCities <= minReachableCities:
36                minReachableCities = reachableCities
37                bestCity = i
38        
39        return bestCity