class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #basic idea -> open < close 
        stack =[]
        res=[]
        def track(open,close):
            if open==close==n:
                res.append("".join(stack))
                return
            if open< n:
                stack.append("(")
                track(open+1,close)
                stack.pop()
            if close < open:
                stack.append(")")
                track(open,close+1)
                stack.pop()
        track(0,0)
        return res