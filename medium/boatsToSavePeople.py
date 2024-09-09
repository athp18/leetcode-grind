class Solution: 
  # the basic intuition here is to pair the heaviest and lightest person together. so we sort the array and do a 2 pointers solution
  # basically, we keep on moving our two pointers while we're under the limit. when/if we reach the limit, we decrement the right pointer (which corresponds to the heavier person)
  # finally, we increment the count variable
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        count = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            count += 1
        return count
