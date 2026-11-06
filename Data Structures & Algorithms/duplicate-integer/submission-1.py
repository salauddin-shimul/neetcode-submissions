class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dup = list(set(nums))
        return len(no_dup) != len(nums)