class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scores = sorted(score, reverse=True)
        rank = {}
        for i, s in enumerate(scores):
            if i == 0:
                rank[s] = 'Gold Medal'
            elif i == 1:
                rank[s] = 'Silver Medal'
            elif i == 2:
                rank[s] = 'Bronze Medal'
            else:
                rank[s] = str(i+1)
        
        answer = [rank[s] for s in score]
        return answer
