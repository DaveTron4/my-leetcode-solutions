from collections import deque

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        i, j = len(a) - 1, len(b) - 1

        result = deque()
        carry = 0

        while i >= 0 or j >= 0 or carry:

            val1 = int(a[i]) if i >= 0 else 0
            val2 = int(b[j]) if j >= 0 else 0

            total = val1 + val2 + carry

            binary = total % 2

            carry = total // 2

            result.appendleft(str(binary))
            
            i -= 1
            j -= 1


        result = "".join(result)
        return result

            