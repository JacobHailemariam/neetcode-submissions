class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dictionaries = []
        groups = defaultdict(list)
        for word in strs:
            count = [0] * 26                      # one slot per letter a-z
            for c in word:
                count[ord(c) - ord('a')] += 1     # 'a'->0, 'b'->1, ... 'z'->25
            groups[tuple(count)].append(word)
        return list(groups.values())
           

                 
            
            
                
    