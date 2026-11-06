class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_tracker = {}
        for index, number in enumerate(nums):
            complement = target - number
            if complement in num_tracker:
                return [num_tracker[complement], index]
            num_tracker[number] = index
