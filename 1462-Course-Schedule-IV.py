class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        canTake = [[False] * numCourses for _ in range(numCourses)]

        for pre, course in prerequisites:
            canTake[pre][course] = True

        for mid in range(numCourses):
            for src in range(numCourses):
                for dst in range(numCourses):
                    canTake[src][dst] = canTake[src][dst] or (canTake[src][mid] and canTake[mid][dst])
        
        return [canTake[u][v] for u, v in queries]
        