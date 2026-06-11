class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        #use a hashset
        hashmap = {}
        
        for i, n in enumerate(nums):
            if target - n in hashmap.keys():
                return [hashmap[target - n], i]
            hashmap[n] = i
        return[-1,-1]
