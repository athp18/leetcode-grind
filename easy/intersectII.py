class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        for num in nums1:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        res = []
        for k in nums2:
            if k in hashmap and hashmap[k] > 0:
                res.append(k)
                hashmap[k] -= 1
        return res
