class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0

        def dfs(row, col):

            if (
                row < 0
                or col < 0
                or row >= len(grid)
                or col >= len(grid[0])
                or grid[row][col] == 0
            ):
                return 0

            grid[row][col] = 0

            return (
                1
                + dfs(row + 1, col)
                + dfs(row - 1, col)
                + dfs(row, col + 1)
                + dfs(row, col - 1)
            )

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    max_area = max(area, max_area)

        return max_area
