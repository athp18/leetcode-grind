class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])  # Sort by start time
        merged = [intervals[0]] 

        for current_interval in intervals[1:]:
            last_merged_interval = merged[-1]

            if current_interval[0] <= last_merged_interval[1]:
                last_merged_interval[1] = max(last_merged_interval[1], current_interval[1])
            else:
                merged.append(current_interval)
        
        return merged
