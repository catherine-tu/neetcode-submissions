class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # approach: dfs for each unexplored 1, look for surrounding 1s
        visited = set() # of tuples (i, j)
        count = 0
        n = len(grid) - 1
        m = len(grid[0]) - 1

        # find all neighboring 1s
        def dfs(i, j):

            # check if in bounds
            if (i > n or i < 0 or j > m or j < 0 or grid[i][j] == '0' or (i, j) in visited):
                return

            visited.add((i, j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        for i, lis in enumerate(grid):
            for j, char in enumerate(lis):
                # if not visited yet, start a dfs on it
                if (i, j) not in visited and grid[i][j] == '1': 
                    count += 1
                    dfs(i, j)
        
        return count




        # # approach: dfs

        # if not grid:
        #     return False

        # def dfs(i, j):
        #     # if oob or not part of an island
        #     if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
        #         return
            
        #     grid[i][j] = '0' # mark as visited
        #     dfs(i + 1, j)
        #     dfs(i-1, j)
        #     dfs(i, j+1)
        #     dfs(i, j-1)

        # # loop through, and for each unexplored 1, call dfs
        # count = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == '1':
        #             count += 1
        #             dfs(i, j)
        
        # return count