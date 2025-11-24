class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I' : 1 , 'V' : 5 , 'X' : 10 , 'L' : 50 , 'C' : 100 , 'D' : 500 , 'M' : 1000 }

        sum = 0
        prev = 0

        for i in reversed(s):
            value = roman[i]
            if value < prev:
                sum -= value 
                prev = value
            else:
                sum += value 
                prev = value

        return sum