import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        
        def count_smaller_fractions(target):
            count, j = 0, 1
            MAX = [0, 1]
            for i in range(n - 1):
                while j < n and arr[i] > target * arr[j]:
                    j += 1
                count += n - j
                if j < n and arr[i] / arr[j] > MAX[0] / MAX[1]:
                    MAX = [arr[i], arr[j]]
            return count, MAX
        
        l, r = 0, 1
        while r - l > 1e-9:
            mid = (l + r) / 2
            count, fraction = count_smaller_fractions(mid)
            if count < k:
                l = mid
            else:
                r = mid
                if count == k:
                    return fraction
        return fraction
