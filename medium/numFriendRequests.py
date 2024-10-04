from collections import Counter

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def canSend(age_x, age_y):
            return not (age_y <= 0.5 * age_x + 7 or age_y > age_x or (age_y > 100 and age_x < 100))
        
        hashmap, requests = Counter(ages), 0
      
        for age_x in hashmap:
            for age_y in hashmap:
                if canSend(age_x, age_y):
                    if age_x == age_y:
                        requests += hashmap[age_x] * (hashmap[age_y] - 1)
                    else:
                        requests += hashmap[age_x] * hashmap[age_y]
        return requests
