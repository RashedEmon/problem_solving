class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        laser_per_row = []

        for row in bank:
            total_laser_in_row = 0
            for c in row:
                if c == "1":
                    total_laser_in_row += 1
            if total_laser_in_row > 0:
                laser_per_row.append(total_laser_in_row)

        res = 0
        for i in range(1,len(laser_per_row)):
            res += laser_per_row[i]*laser_per_row[i-1]
        
        return res
    
