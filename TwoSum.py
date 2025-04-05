# https://leetcode.com/problems/two-sum/
from typing import List

# nums = [2,7,11,15]
# target = 9

# nums = [3, 2, 4]
# target = 6

# nums = [3, 3]
# target = 6


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        begin_i = 0
        end_i = len(sorted_nums) - 1
        while begin_i < end_i:
            if sorted_nums[begin_i] + sorted_nums[end_i] > target:
                end_i -= 1
            elif sorted_nums[begin_i] + sorted_nums[end_i] < target:
                begin_i += 1
            else:
                for i in range(len(nums)):
                    if nums[i] in [sorted_nums[begin_i], sorted_nums[end_i]]:
                        for j in range(i + 1, len(nums)):
                            if nums[j] in [sorted_nums[begin_i], sorted_nums[end_i]]:
                                return [i, j]
        return "not solution"


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            n = target - nums[i]
            if myDict.get(n) and myDict[n] != i:
                return [i, myDict[n]]
        return "not solution"


sol = Solution()
print(sol.twoSum(nums, target))
