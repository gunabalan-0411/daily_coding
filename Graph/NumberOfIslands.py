import collections
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        # no of islands
        islands = 0
        # set to store visited islands or lands
        visited = set()

        # breadth first search to trace the graph structure
        def bfs(r, c):
            # initialize queue data structure
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                # search in four directions
                for dr, dc in directions:
                    r, c = (row + dr), (col + dc)
                    if (r in range(rows) and
                       c in range(cols) and
                       grid[r][c] == '1' and
                       (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands
