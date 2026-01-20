class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a =s.split(' ')

        for i in range(len(a)-1,-1,-1):
            if len(a[i]) != 0:
                return len(a[i])