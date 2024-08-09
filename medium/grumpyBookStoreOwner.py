class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfied += customers[i]
        MAX, curr = 0, 0
        for i in range(minutes):
            if grumpy[i] == 1:
                curr += customers[i]
        MAX = curr
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                curr += customers[i]
            if grumpy[i - minutes] == 1:
                curr -= customers[i - minutes]
            MAX = max(MAX, curr)
        return satisfied + MAX
