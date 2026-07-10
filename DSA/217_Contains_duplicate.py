

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for x in nums:
            if x in s: return True
            s.add(x)
        
        return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)

        return len(unique) != len(nums)