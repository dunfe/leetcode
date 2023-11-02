from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, n in enumerate(nums):
            if target - n in d:
                return [d[target - n], i]
            d[n] = i
        return []


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
