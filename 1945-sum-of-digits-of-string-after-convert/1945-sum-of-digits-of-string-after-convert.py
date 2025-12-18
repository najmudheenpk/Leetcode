class Solution:
    def getLucky(self, s: str, k: int) -> int:

        sample = ""
        for ch in s:
            sample += str(ord(ch) - 96)


        for _ in range(k):
            total = 0
            for digit in sample:
                total += int(digit)
            sample = str(total)

        return int(sample)
