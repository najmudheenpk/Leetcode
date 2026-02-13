class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        missing =  []
        numMax = max(nums)
        numMin = min(nums)
        for i in range(numMin,numMax+1):
            if i not in nums:
                missing.append(i)

        return missing