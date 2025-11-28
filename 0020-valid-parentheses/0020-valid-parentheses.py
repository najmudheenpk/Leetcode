class Solution:
    def isValid(self, s: str) -> bool:
        dct = {')' : '(' , '}' : '{' , ']' : '['}
        arr = []
        for i in s:
            if i in dct.values():
                arr.append(i)
            elif i in dct:
                if not arr or arr.pop() != dct[i]:
                    return False
            else:
                return False

        return not arr

