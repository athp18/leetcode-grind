class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort() # time complexity O(n log n)

        res = []
        prefix = ""

        for char in searchWord:
            prefix += char
            i = self.binarySearch(products, prefix)
            temp = []

            for word in products[i:i+3]:
                if word.startswith(prefix):
                    temp.append(word)
            
            res.append(temp)
        return res
    
    def binarySearch(self, arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            #if arr[mid] == target:
                #return mid
            if arr[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
