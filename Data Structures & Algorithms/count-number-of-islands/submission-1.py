class Solution:           
    def dfs(self, x, y, grid) -> None:
        lrow = len(grid)
        lcol = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        position = (x,y)
        grid[x][y] = '2'
        stack = [position]
        while stack:
            cx, cy = stack.pop()
            for x, y in directions:
                nx, ny = cx+x, cy+y
                if nx>=0 and ny>=0 and nx<lrow and ny<lcol:
                    if grid[nx][ny] == '1':
                        grid[nx][ny] = '2'
                        aux = (nx,ny)
                        stack.append(aux)

    def numIslands(self, grid: List[List[str]]) -> int:
        stack = []
        
        countIsland = 0
        lrow = len(grid)
        lcol = len(grid[0])
        for row in range(lrow):
            for col in range(lcol):
                if grid[row][col] == '1':                  
                    self.dfs(row,col,grid)
                    countIsland += 1
        return countIsland