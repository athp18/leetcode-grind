class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: # brute force solution: O(n^2) time complexity
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
        return result


class Solution: # O(n) time complexity & O(n) space complexity. Here, we create a stack and pop it if we find a greater value, then append it to the result
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                result[i] = stack[-1] - i
            stack.append(i)
        return result



            

            
