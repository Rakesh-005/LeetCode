from collections import defaultdict
import heapq

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Build adjacencies
        adjs = defaultdict(list)
        for a, b in edges:
            adjs[a].append(b)
            adjs[b].append(a)
        
        # Map each node to its level
        levels_by_node = dict()
        q = deque([0])
        seen = set()
        level = 0
        while q:
            for _ in range(len(q)):
                x = q.popleft()
                seen.add(x)
                levels_by_node[x] = level
                for adj in adjs[x]:
                    if adj not in seen:
                        q.append(adj)
            level += 1

        # Calculate Bob's path
        bob_path = []
        q = deque([bob])
        while q:
            x = q.popleft()
            bob_path.append(x)
            for adj in adjs[x]:
                if levels_by_node[adj] == levels_by_node[x] - 1:
                    q.append(adj)

        # Do BFS from Alice's perspective
        q = deque([(0,0)]) # (node, total_score)
        level = 0
        bob_idx = 0
        best = -inf
        while q:
            if bob_idx < len(bob_path):
                amount[bob_path[bob_idx]] //= 2
            for _ in range(len(q)):
                x, score = q.popleft()
                score += amount[x]
                is_leaf = True
                for adj in adjs[x]:
                    if levels_by_node[adj] == levels_by_node[x] + 1:
                        q.append((adj, score))
                        is_leaf = False
                if is_leaf:
                    best = max(best, score)
            if bob_idx < len(bob_path):
                # Not strictly necessary, since we won't be returning to the node
                amount[bob_path[bob_idx]] = 0
                bob_idx += 1

        return best
               