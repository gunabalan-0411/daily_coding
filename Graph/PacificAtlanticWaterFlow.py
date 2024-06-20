class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROW = len(heights)
        COL = len(heights[0])
        # set to store the coordinates that can be reach from respective
        # oceans
        pacific, atlantic = set(), set()

        # depth first search to find the coordinate
        def dfs(r, c, visit, prevHeight):
            # base condition to exit
            if (
                # if already visited the coordinates hence 
                # further avoid repeated steps
                (r, c) in visit or
                # out of bounds cases
                r < 0 or c < 0 or r == ROW or c == COL or
                # if it couldn't move forward
                heights[r][c] < prevHeight
            ):
                return
            # if it passes the above condition then add 
            # it to the respective visit
            visit.add((r, c))
            # -- Now have to move in all four direction to trace
            dfs(r-1, c, visit, heights[r][c]) # up
            dfs(r+1, c, visit, heights[r][c]) # down
            dfs(r, c+1, visit, heights[r][c]) # right
            dfs(r, c-1, visit, heights[r][c]) # left
        # check if from top and bottom row how far we can reach
        for c in range(COL):
            # Initialy set the same value as previous height
            dfs(0, c, pacific, heights[0][c]) # from pacific
            dfs(ROW-1, c, atlantic, heights[ROW-1][c]) # from atlantic
        # check if from left and right side of the island how far we can reach
        for r in range(ROW):
            dfs(r, 0, pacific, heights[r][0]) # from pacific
            dfs(r, COL-1, atlantic, heights[r][COL-1]) # from atlantic
        res = []
        # looping to capture the coordinates to where we can reach from both sea
        for r in range(ROW):
            for c in range(COL):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res

        

            


        