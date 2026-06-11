class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        q_pacific = deque()
        q_atlantic = deque()

        for r in range(rows):
            q_pacific.append((r, 0))
            q_atlantic.append((r, cols - 1))
        
        for c in range(cols):
            q_pacific.append((0, c))
            q_atlantic.append((rows - 1, c))

        def bfs_pacific(r, c):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr in range(rows) and nc in range(cols) and (nr, nc) not in pacific and heights[r][c] <= heights[nr][nc]:
                    q_pacific.append((nr, nc))
                    pacific.add((nr, nc))
                
        def bfs_atlantic(r, c):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr in range(rows) and nc in range(cols) and (nr, nc) not in atlantic and heights[r][c] <= heights[nr][nc]:
                    q_atlantic.append((nr, nc))
                    atlantic.add((nr, nc))


        while q_pacific:
            for i in range(len(q_pacific)):
                r, c = q_pacific.popleft()
                pacific.add((r, c))
                bfs_pacific(r, c)
        

        while q_atlantic:
            for i in range(len(q_atlantic)):
                r, c = q_atlantic.popleft()
                atlantic.add((r, c))
                bfs_atlantic(r, c)
        res = []
        for (r, c) in atlantic:
            if (r, c) in pacific:
                res.append([r, c])

        return res

        
        