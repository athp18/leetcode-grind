class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curr = sum(cardPoints[:k])
        MAX = curr

        for i in range(1, k+1):
            curr += cardPoints[-i] - cardPoints[k-i]
            MAX = max(MAX, curr)
        
        return MAX
