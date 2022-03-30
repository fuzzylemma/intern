#!/usr/bin/python3

List = list

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, k, n = 0, 0, 1, len(nums)
        while j < n:
            if nums[i] != nums[j]:
                nums[k] = nums[j]
                i = j
                k += 1
            j += 1
        return k 


if __name__ == "__main__":
    solution = Solution()
    case_1 = [1,1,2]
    case_1_ans = solution.removeDuplicates(case_1)
    case_2 = [0,0,1,1,1,2,2,3,3,4]
    case_2_ans = solution.removeDuplicates(case_2)

    print(case_1[:case_1_ans])
    print(case_2[:case_2_ans])
