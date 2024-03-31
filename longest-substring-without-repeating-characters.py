### use variable length sliding window technique. maintain a window list and window set. 
### duplicate check using set when duplicate found then remove element from start 
### while duplicate value not found from window list. store max list after each iteration.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        if len(s)==0:
            return 0
        unique_list = set()
        window_list = []
        for i in s:
            if i in unique_list:
                while True:
                    element = window_list.pop(0)
                    unique_list.remove(element)
                    if element==i:
                        break
                unique_list.add(i)
                window_list.append(i)
            else:
                unique_list.add(i)
                window_list.append(i)
            res = max(len(unique_list), res)
        return res
