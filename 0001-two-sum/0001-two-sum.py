class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_dict = dict()

        for i , num in enumerate(nums):
            if target - num in prev_dict:
                return [i , prev_dict[target - num]]
            prev_dict[num] = i
        return -1