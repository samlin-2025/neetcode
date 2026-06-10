class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r,c))
        
        def infectNeighbors(r, c):
            if r in range(rows) and c in range(cols) and (r, c) not in visited and grid[r][c] == 1:
                grid[r][c] = 2
                visited.add((r, c))
                q.append((r, c))


        t = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                infectNeighbors(r + 1, c)
                infectNeighbors(r - 1, c)
                infectNeighbors(r, c + 1)
                infectNeighbors(r, c - 1)
            if q: t += 1 #only count if new oranges were infected
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1


        return t
