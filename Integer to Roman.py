#leetcode #medium #STRING

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
    
        roman=""
        number = num
        while number>0:
            if number < 5 and number>0:
                if number == 4:
                    roman+="IV"
                else:
                    roman+="I"*number
                number=0
                continue
            elif (number < 10 and number >= 5):
                if number>=9:
                    roman+="IX"
                    number=number%9
                else:
                    roman+="V"
                number=number%5
                continue
            elif number< 50 and number >= 10:
                if number >= 40:
                    roman+="XL"
                    number=number%40
                    continue
                roman+="X" * (number//10)
                number=number%10
            elif number < 100 and number >= 50:
                if number >= 90:
                    roman+="XC"
                    number=number%90
                    continue
                roman+="L"
                number=number%50
            elif number < 500 and number >= 100:
                if number >= 400:
                    roman+="CD"
                    number=number%400
                    continue
                roman+="C" * (number//100)
                number=number%100
            elif number < 1000 and number >= 500:
                if number >= 900:
                    roman+="CM"
                    number=number%900
                    continue
                roman+="D"
                number=number%500
            elif number >= 1000:
                roman+="M"*(number//1000)
                number=number%1000
        return roman
