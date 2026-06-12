class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def dfs(currString, openCount, closedCount):
            if openCount + closedCount == 2 * n:
                res.append(currString)
                return
            
            
            if openCount < n:
                dfs(currString + '(', openCount + 1, closedCount)

            if closedCount < openCount:
                
                dfs(currString + ')', openCount, closedCount + 1)
            
        dfs("", 0, 0)
        return res
        
                