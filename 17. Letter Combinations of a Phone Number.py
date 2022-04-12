class Solution(object):
    letterMap = {
        "2": ['a', 'b', 'c'],
        "3": ['d', 'e', 'f'],
        "4": ['g', 'h', 'i'],
        "5": ['j', 'k', 'l'],
        "6": ['m', 'n', 'o'],
        "7": ['p', 'q', 'r', 's'],
        "8": ['t', 'u', 'v'],
        "9": ['w', 'x', 'y', 'z'],
    }

    result = []

    def letterCombinations(self, digits):
        self.result=[]
        if digits=="":
            return []
        self.solve(digits, 0, "")
        return self.result

    def solve(self, digits, index, path):
        if index == len(digits):
            self.result.append(path)
            return
        for i in self.letterMap[digits[index]]:
            self.solve(digits, index+1, path+i)
        return
