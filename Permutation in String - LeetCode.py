class Solution:
    def __init__(self):
        self.dict1 = {}
        self.dict2 = {}

    def checkInclusion(self, s1: str, s2: str) -> bool:
        for char in s1:
            self.add_to_dict(char, self.dict1)
        
        start = 0
        end = len(s1) - 1
        for char in s2[start: end+1]:
            self.add_to_dict(char, self.dict2)

        while True:
            if self.compare_two_dict():
                return True
            else:
                self.remove_from_dict(s2[start], self.dict2)
                start+=1
                end+=1
                if end >= len(s2):
                    break
                self.add_to_dict(s2[end], self.dict2)
        return False        
            

    def compare_two_dict(self):
        for key, value in self.dict1.items():
            if not (key in self.dict2 and value == self.dict2[key]):
                return False
        return True

    def add_to_dict(self, char, dict2):
        if char in dict2:
            dict2[char] += 1
        else:
            dict2[char] = 1

    def remove_from_dict(self, char, dict2):
        if char in dict2:
            if dict2[char] > 1:
                dict2[char] -= 1
            else:
                del dict2[char]
