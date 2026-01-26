class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [a - b for a, b in zip(gas, cost)]
        
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start_idx = 0
        for i in range(len(diff)):
            total += diff[i]

            if total < 0:
                total = 0
                start_idx = i + 1

                
        return start_idx

                
           
        