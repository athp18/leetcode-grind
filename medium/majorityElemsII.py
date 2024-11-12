class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        majority_elems = []
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            if hashmap[num] > len(nums) // 3 and num not in majority_elems:
                majority_elems.append(num)
        return majority_elems
