class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ai = {}
        for i, num in enumerate(nums):
            q = target - num
            if q in ai:
                return [ai[q], i]
            ai[num] = i
        return []
