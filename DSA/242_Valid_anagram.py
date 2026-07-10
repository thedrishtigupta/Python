
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False
        
        freq = defaultdict(int)

        for x in s: freq[x] += 1

        for x in t: freq[x] -= 1

        for it in freq:
            if freq[it] : return False

        return True

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False

        freq1, freq2 = Counter(s), Counter(t)

        return freq1 == freq2