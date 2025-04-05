class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for ind,i in enumerate(nums):
            hashmap[i]=ind
        for j in range(len(nums)):
            diff=target-nums[j]
            if diff in hashmap and hashmap[diff]!=j:
                return [j, hashmap[diff]]
        return []
