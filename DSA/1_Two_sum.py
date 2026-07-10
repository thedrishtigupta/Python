

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = dict()

        for i, a in enumerate(nums):
            b = target - a
            if b in mp: return [mp[b], i]
            else : mp[a] = i
        
        return [0, 0]
        