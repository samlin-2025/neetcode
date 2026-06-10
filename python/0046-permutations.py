class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        res = []
       


        def backtrack(curArr, filled):
            if(len(curArr) == len(nums)):
                res.append(curArr.copy())


            for i, n in enumerate(nums):
                if filled[i]:  # skip already-used numbers
                    continue
                filled[i] = True
                curArr.append(n)
                backtrack(curArr, filled)
                curArr.pop()
                filled[i] = False


   
        backtrack([], [False] * len(nums))
        return res



