class Solution:
    def reverseBits(self, n: int) -> int:
        binary_val = (bin(n)[2:]).zfill(32)

        reversed_bit = binary_val[::-1]

        return int(reversed_bit, 2)