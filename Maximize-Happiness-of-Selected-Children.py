1class Solution:
2    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
3        # Convert the list into a max heap by inverting the happiness values 
4        # Python's default heap data structure is a min heap
5        max_heap = [-h for h in happiness]
6        heapq.heapify(max_heap)
7        
8        total_happiness_sum = 0
9        turns = 0
10
11        for i in range(k):
12            # Invert again to get the original value
13            total_happiness_sum += max(-heapq.heappop(max_heap) - turns, 0)
14
15            # Increment turns for the next iteration
16            turns += 1
17            
18        return total_happiness_sum
19