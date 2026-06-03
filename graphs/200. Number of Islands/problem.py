from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if grid is None: return 0

        rows, col = len(grid), len(grid[0])  # get grid dimensions
        visted = set()                        # tracks every cell we've already seen
        islands = 0                           # counter we increment per island found

        def bfs(r, c):
            q = deque()
            visted.add((r, c))   # mark starting cell visited before we even enter the loop
            q.append((r, c))     # push starting cell into the queue

            while q:             # keep going until no more connected land to explore
                row, col = q.popleft()  # take the next cell off the front of the queue

                directions = [[1,0], [-1,0], [0,1], [0,-1]]  # down, up, right, left

                for dr, dc in directions:
                    r, c = row + dr, col + dc   # calculate neighbor cell coordinates

                    if (r in range(row) and    # neighbor is inside grid vertically
                        c in range(col) and     # neighbor is inside grid horizontally
                        grid[r][c] == "1" and   # neighbor is land not water
                        (r,c) not in visted):   # neighbor hasn't been visited yet
                        q.append((r, c))        # add neighbor to queue to explore next
                        visted.add((r, c))      # mark it visited now so nothing else adds it twice

        for r in range(rows):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visted:  # found unvisited land
                    bfs(r, c)    # flood fill the entire island marking everything visited
                    islands += 1 # once bfs returns the whole island is consumed, count it

        return islands


grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

sol = Solution()
print(sol.numIslands(grid))



        


"""
This is how I am trying to think of how to do this:
For starters I think it would be good to us to use a BFS algorithm for this. 

so first we need to make sure that if there is actually something within the grid. 

check to see if the grid is empty.

From there we are going to create rows and colums from the grid. 
Also we are going to be use a visit to make sure that it has checked the node.
Also count how many islands there actually are. 

create the bfs function

then create a for loop to check the islands
"""