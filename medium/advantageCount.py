class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums1.sort()

        indexed_nums2 = [(nums2[i], i) for i in range(n)]
        indexed_nums2.sort()

        result = [0] * n
        left, right = 0, n -1
        for i in range(n-1, -1, -1):
            num2, original_index = indexed_nums2[i]
            if nums1[right] > num2:
                result[original_index] = nums1[right]
                right -= 1
            else:
                result[original_index] = nums1[left]
                left += 1
            
        return result
