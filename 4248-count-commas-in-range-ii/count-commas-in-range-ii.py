class Solution:
    def countCommas(self, n: int) -> int:  
        total_commas = 0
        current_tier = 1000
        
        while n >= current_tier:
            total_commas += (n - current_tier + 1)
            
            current_tier *= 1000
            
        return total_commas