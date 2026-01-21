class Solution:
    def hammingWeight(self, n: int) -> int:
        
        bitn = bin(n)[2:]
        count = 0

        for bit in bitn:
            if bit == "1":
                count += 1
        
        return count