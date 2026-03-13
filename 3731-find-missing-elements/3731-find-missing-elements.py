class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        output =[]
        for i in range(min(nums) , max(nums)+ 1):
            if i not in nums:
                output.append(i)
        return output