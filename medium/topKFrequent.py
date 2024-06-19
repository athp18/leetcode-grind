class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        hashlist = (sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        reslst = [item[0] for item in hashlist[:k]]
        return reslst
