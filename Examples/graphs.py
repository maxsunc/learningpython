# this file contains all my solutions to graph problems
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # matrix BFS/DFS
        # 1st step: iterate through the matrix and find 1 value
        visited = set() # set of tuples
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        result = 0
        def validCoord(coord, matrix):
            return 0 <= coord[0] < len(matrix) and 0 <= coord[1] < len(matrix[0])
        def dfs(row, i):
            if grid[row][i] == "0":
                return
            # we know this value is a one, so we need to call dfs on all directions
            for direction in directions:
                coord = (direction[0] + row, direction[1] + i)
                if(not validCoord(coord,grid) or coord in visited):
                    continue
                visited.add(coord)
                dfs(coord[0], coord[1])
                
        def bfs(row, i):
            queue = deque() # ()
            queue.append((row,i))
            while queue:
                currentCoord = queue.popleft()
                # move left, right, up, down
                for direction in directions:
                    coord = (direction[0] + currentCoord[0], direction[1] + currentCoord[1])
                    # check if coord is a valid coordinate
                    if(not validCoord(coord,grid) or coord in visited):
                        continue
                    visited.add(coord)
                    # check if its a 1 then add it to queue
                    if grid[coord[0]][coord[1]] == "1":
                        queue.append(coord)
        # iterate the matrix
        for row in range(0,len(grid)):
            for i in range(0,len(grid[row])):
                if((row,i) in visited):
                    continue
                visited.add((row,i))
                if grid[row][i] == "1":
                    print(f"found a 1 at {(row,i)}")
                    result += 1
                    # perform the bfs to search for how large the island is:
                    dfs(row, i)

                    
                else:
                    print('found 0')
        return result
#     ["1","1","0","0","1"],
#     ["1","1","0","0","1"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]

def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs to check how big the island is
        
        # iterate the grid
        # find a 1
        # find how large that island is
        # set of visited squares
        # 
        # dfs
        directions = [(0,1),(0,-1), (1,0), (-1,0)]
        seen = set()
        result = 0

        def validCoord(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        def bfs(row, i):
            queue = deque() # ()
            queue.append((row,i))
            numOnes = 1
            while queue:
                currentCoord = queue.popleft()
                print('blah')
                # move left, right, up, down
                for direction in directions:
                    coord = (direction[0] + currentCoord[0], direction[1] + currentCoord[1])
                    # check if coord is a valid coordinate
                    if(not validCoord(coord[0],coord[1]) or coord in seen):
                        continue
                    seen.add(coord)
                    # check if its a 1 then add it to queue
                    if grid[coord[0]][coord[1]] == 1:
                        queue.append(coord)
                        numOnes += 1
            return numOnes
        def dfs(coordinates):
            r = coordinates[0]
            c = coordinates[1]
            # returns the size of the body of one found
            seen.add((r,c))
            if grid[r][c] == 0:
                return 0

            ic = []
            numOne = 1
            # check in each direction if there is a one
            for direction in directions:
                coord = (r + direction[0], c + direction[1])
                if not validCoord(coord[0],coord[1]) or coord in seen:
                    continue
                seen.add(coord)
                # check if this coordinate is a 1
                ic.append(coord)
            for coord in ic:
                numOne += dfs(coord)
            
            return numOne
            

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] in seen:
                    continue
                seen.add((row,col))

                # check if its a 1 so we can check the size
                if grid[row][col] == 1:
                    # we've hit an island
                    # check how big the island is
                    # size = dfs((row,col))
                    size = bfs(row, col)
                    result = max(result, size)
        return result
# [0,0,1,0,0,0,0,1,0,0,0,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,1,1,0,1,0,0,0,0,0,0,0,0],
# [0,1,0,0,1,1,0,0,1,0,1,0,0],
# [0,1,0,0,1,1,0,0,1,1,1,0,0],
# [0,0,0,0,0,0,0,0,0,0,1,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,0,0,0,0,0,0,1,1,0,0,0,0]