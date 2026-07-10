
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        sum = 0
        ans = 0

        for x in nums:
            sum += x

            if sum == k : ans += 1

            rem = sum - k

            if mp[rem] : ans += mp[rem]

            mp[sum] += 1
        
        return ans