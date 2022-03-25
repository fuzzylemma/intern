#!/usr/bin/python3

List = list

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, ele in enumerate(nums):
            temp = target-ele
            if temp in memo:
                return [ memo[temp], i ]
            memo[ele] = i
        return [0,0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2,7,11,15], 9))
    print(solution.twoSum([3,2,4], 6))
    print(solution.twoSum([3,3], 6))
