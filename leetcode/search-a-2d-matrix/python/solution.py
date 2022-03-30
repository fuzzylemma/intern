#!/usr/bin/python3

List = list

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        i, j = 0, 0 
                    
        while i < n and j < m:
            if matrix[i][j] == target:
                return True
                                               
            if i+1 < n and matrix[i+1][j] <= target:
                i += 1
                continue
                                                                      
            if j+1 < m and matrix[i][j+1] <= target:
                j += 1
                continue
         
            return False 
        return False


if __name__ == "__main__":
  solution = Solution()
  print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],  3))
  print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],  13))
