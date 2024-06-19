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
