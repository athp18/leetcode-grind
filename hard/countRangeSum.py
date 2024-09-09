class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def mergeSort(start, end):
            if start >= end:
                return 0
            
            mid = (start + end) // 2
            count = mergeSort(start, mid) + mergeSort(mid + 1, end)
            
            j = k = mid + 1
            for i in range(start, mid + 1):
                while j <= end and prefixSum[j] - prefixSum[i] < lower:
                    j += 1
                while k <= end and prefixSum[k] - prefixSum[i] <= upper:
                    k += 1
                count += k - j
            
            temp = []
            left, right = start, mid + 1
            while left <= mid and right <= end:
                if prefixSum[left] <= prefixSum[right]:
                    temp.append(prefixSum[left])
                    left += 1
                else:
                    temp.append(prefixSum[right])
                    right += 1
            
            temp.extend(prefixSum[left:mid+1])
            temp.extend(prefixSum[right:end+1])
            prefixSum[start:end+1] = temp
            
            return count
        
        prefixSum = [0] + list(accumulate(nums))
        return mergeSort(0, len(prefixSum) - 1)
