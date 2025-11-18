class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for val in nums:
            decision = max(val+rob1 , rob2)

            rob1 = rob2
            rob2 = decision 

        
        return rob2