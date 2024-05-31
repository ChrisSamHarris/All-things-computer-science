
from collections import Counter

class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        count = 0 
        
        words1_hm = Counter(words1)
        words2_hm = Counter(words2)

        for word in words1_hm.keys():
            if words1_hm[word] == 1 and words2_hm[word] == 1:
                count +=1 

        return count 
    
match_words = Solution().countWords(words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"])
print(match_words)


## Counter function 
def count_occurrences(words):
        counts = {}
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return counts