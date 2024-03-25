class Solution:
    def __init__(self):
        self.result = []
    def generateParenthesis(self, n: int) -> List[str]:
        self.solve(n-1, n, "(")
        return self.result

    def solve(self, o: int, c: int, s: str):
        if o > c:
            return
        
        if c == 0 and o == 0:
            self.result.append(s)
            return
        if o > 0:
            self.solve(o-1, c, s+"(")
        if c > 0:
            self.solve(o, c-1, s+")")

