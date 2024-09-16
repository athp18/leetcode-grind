class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        def canAchieveMinPower(minPower: int) -> bool:
            n = len(stations)
            added_stations = [0] * n
            current_power = 0
            additional_needed = 0
            
            # Calculate the initial power for the first window of size `r`
            for i in range(min(r + 1, n)):
                current_power += stations[i]
            
            # Sliding window to maintain the power sum over the cities
            for i in range(n):
                # check if current city has enough power
                if current_power < minPower:
                    add_needed = minPower - current_power
                    additional_needed += add_needed
                    if additional_needed > k:
                        return False
                    # Add the stations at the farthest city within range
                    if i + r < n:
                        added_stations[i + r] += add_needed
                    current_power += add_needed
                
                # slide to the right
                if i + r + 1 < n:
                    current_power += stations[i + r + 1]
                if i - r >= 0:
                    current_power -= stations[i - r] + added_stations[i - r]
            
            return True
        
        # Binary search on the answer
        left, right = 0, sum(stations) + k
        while left < right:
            mid = (left + right + 1) // 2
            if canAchieveMinPower(mid):
                left = mid
            else:
                right = mid - 1
        
        return left
