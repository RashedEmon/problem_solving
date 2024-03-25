class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = False
        if divisor < 0:
            divisor = abs(divisor)
            is_negative = not is_negative
        
        if dividend < 0:
            dividend = abs(divisor)
            is_negative = not is_negative

        res = 0
        while dividend >= divisor:
            dividend = dividend - divisor
            res+=1
        return -res if is_negative else res
