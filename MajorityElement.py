from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        t=len(nums)//2
        freq=Counter(nums)
        for k,v in freq.items():
            if v> t:
                return k
