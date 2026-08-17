class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # greedy approach: see when tank (tank + gas - cost) > 0

        # if this is false, we already know a solution exists.
        if sum(gas) < sum(cost):
            return -1

        tank = 0
        idx = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                idx = i + 1
        
        return idx

        # # special case
        # if sum(gas) < sum(cost): 
        #     return -1

        # tank = 0 # current gas in tank
        # idx = 0 # current starting index

        # # accounting for the gas & cost 
        # for i in range(len(gas)):
        #     tank += gas[i] - cost[i]

        #     # if you cant reach station i+1 from here
        #     if tank < 0:
        #         tank = 0
        #         # next possible station is after the failure
        #         idx = i+1

        # return idx