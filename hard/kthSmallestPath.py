class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        v, h = destination
        total = v + h
        
        result = []
        remaining_v = v
        remaining_h = h
        
        def nCr(n, r):
            if r > n - r:
                r = n - r
            res = 1
            for i in range(r):
                res *= (n - i)
                res //= (i + 1)
            return res
        
        for i in range(total):
            if remaining_h == 0:
                result.append('V')
                remaining_v -= 1
            elif remaining_v == 0:
                result.append('H')
                remaining_h -= 1
            else:
                # Calculate number of combinations starting with 'H'
                count_with_h = nCr(remaining_h + remaining_v - 1, remaining_v)
                
                if k <= count_with_h:
                    result.append('H')
                    remaining_h -= 1
                else:
                    result.append('V')
                    remaining_v -= 1
                    k -= count_with_h
        
        return ''.join(result)
