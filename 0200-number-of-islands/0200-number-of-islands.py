"""
1 is land
0 is water

scanning over the matrix and if I find a 1 I will check adjacent 1 from the current index, if i find a zero at a movement in that case we will skip it

Loop the row
    Loop the col

        dfs(row,col)

dfs(row, col):
    Check the edges like row<0 or col < 0 or row>n col > m

    grid[row][col] = 0

    dfs(i+1,j)
    dfs(i-1,j)
    dfs(i,j+1)
    dfs(i,j-1)


"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            if (
                row < 0
                or col < 0
                or row >= len(grid)
                or col >= len(grid[0])
                or grid[row][col] == "0"
            ):
                return

            grid[row][col] = "0"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)

        return count
