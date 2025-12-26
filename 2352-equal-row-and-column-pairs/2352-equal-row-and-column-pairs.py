class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        result=0
        for i in range(len(grid)):
            for j in range(len(grid)):
                match=True
                for k in range(len(grid)):
                    if grid[i][k]!=grid[k][j]:
                        match=False
                        break
                if match:
                    result+=1
        return result