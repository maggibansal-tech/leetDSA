class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<2 or len(nums)>10e4:
            return['list too small or too large'] 
        if target < -10e9 or target > 10e9: 
            return['target too small or large']
        for i in nums:
            if i < -10e9 or i> 10e9:
                return['values too small or too large']
        l=[]
        for i, x in enumerate(nums):
            for j in range(i+1,len(nums)):
                if x+nums[j]==target:
                    l.extend([i,j])
        return l
