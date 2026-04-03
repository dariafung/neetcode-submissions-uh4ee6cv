class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prevMap[crs].append(pre)

        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if prevMap[crs] == []:
                return True

            visit.add(crs)
            for c in prevMap[crs]:
                if not dfs(c):
                    return False
            
            visit.remove(crs)
            prevMap[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        