class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(image)):
            res.append(image[i][::-1])
        for i in range(len(res)):
            res[i] = [1 - x for x in res[i]]
        return res
