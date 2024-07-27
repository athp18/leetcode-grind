class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        sublists = []
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in hashmap:
                hashmap[sorted_word] = 1
                sublists.append([word])
            else:
                hashmap[sorted_word] += 1
                for lst in sublists:
                    if ''.join(sorted(lst[0])) == sorted_word:
                        lst.append(word)
                    else:
                        continue
        return sublists

class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: # more efficient solution
        hashmap = defaultdict(list)
        for s in strs:
            k = ''.join(s)
            hashmap[k].append(s)
        return list(hashmap.values())
