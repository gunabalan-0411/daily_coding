class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # create a pre-requisite adjacency list
        preList = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preList[crs].append(pre)
        
        # Create a visitList to avoid loop
        visitList = set()

        # Depth-first-search algo
        def dfs(crs):
            # Base case to exit
            # If a course is already visited
            if crs in visitList:
                return False
            # If there is no pre-requisite + we make the pre-requisite empty for a course
            # when its pre-requisite is completed
            if preList[crs] == []:
                return True

            visitList.add(crs)
            # iterate all the pre-requisite for a course
            for pre in preList[crs]:
                if not dfs(pre): return False
    
            # Making empty when the above loop completes all pre-requisite
            preList[crs] = []
            # since we finish visiting it
            visitList.remove(crs)
            return True
        # doing dfs for all course, because sometimes two or more disconnected graph
        # may occur
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True


        