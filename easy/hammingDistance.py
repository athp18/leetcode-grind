class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        return bin(z).count('1')
