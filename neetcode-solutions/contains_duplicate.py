class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ax = set()
        for num in nums:
            if num in ax:
                return True
            ax.add(num)
        return False
