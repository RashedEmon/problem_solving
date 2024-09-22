# getting trouble while solving the problem. tried without thinking about edge cases. thinked difficult to add counter more than 10.

class Solution:
    def compress(self, chars: List[str]) -> int:
        res = 0
        counter = 1
        for i in range(1, len(chars), 1):
            if chars[i-1]==chars[i]:
                counter+=1
            else:
                if counter > 1:
                    chars[res] = chars[i-1]
                    res+=1
                    for digit in str(counter):
                        chars[res] = digit
                        res+=1
                else:
                    chars[res] = chars[i-1]
                    res+=1
                
                counter=1
        
        if counter > 1:
            chars[res] = chars[-1]
            res+=1
            for digit in str(counter):
                chars[res] = digit
                res+=1
        if counter == 1:
            chars[res] = chars[-1]
            res+=1

        return res
