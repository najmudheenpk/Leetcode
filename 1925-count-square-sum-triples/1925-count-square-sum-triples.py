class Solution:
    def countTriples(self, n: int) -> int:
        squares = set(i * i for i in range(1, n + 1))
        count = 0

        for c in range(1, n + 1):
            c2 = c * c
            for a in range(1, n + 1):
                if c2 - a * a in squares:
                    count += 1

        return count
