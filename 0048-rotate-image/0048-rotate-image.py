"""

[
    [1,2,3] => [00,01,02] => [20,10,00] => [7,4,1]
    [4,5,6] => [10,11,12] => [21,11,01] => [8,5,2]
    [7,8,9] => [20,21,22] => [22,12,02] => [9,6,3]
]

Increment the row

00 => 02
01 => 12
02 => 22

10 => 01
11 => 11
12 => 21

20 => 00
21 => 10
22 => 20

"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for r in range(n):
            for c in range(r+1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for r in matrix:
            r.reverse()

