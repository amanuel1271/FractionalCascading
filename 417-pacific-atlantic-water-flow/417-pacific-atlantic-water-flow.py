class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights),len(heights[0])
        pacific_queue = deque([])
        atlantic_queue = deque([])
        
        pacific_set = set([(0,c) for c in range(n)] + [(r,0) for r in range(m)])
        for pos in pacific_set:
            pacific_queue.append(pos)
        atlantic_set = set([(m-1,c) for c in range(n)] + [(r,n-1) for r in range(m)])
        for pos in atlantic_set:
            atlantic_queue.append(pos)
            
        
        def bfs(queue,visited):
            
            while queue:
                x,y = queue.popleft()
                for next_x,next_y in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                    if 0 <= next_x < m and 0 <= next_y < n and (next_x,next_y) not in visited:
                        if heights[next_x][next_y] >= heights[x][y]:
                            visited.add((next_x,next_y))
                            queue.append((next_x,next_y))
        
        bfs(pacific_queue,pacific_set)
        bfs(atlantic_queue,atlantic_set)
        
        return list(pacific_set.intersection(atlantic_set))
                
                        
        
                    
        
        
        
        