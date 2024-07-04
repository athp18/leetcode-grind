class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a, 2)
        b = int(b, 2)
        sum_ab = a + b
        sum_ab = bin(sum_ab)[2:]
        return sum_ab
        
