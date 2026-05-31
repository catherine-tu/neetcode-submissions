class Solution:
    def climbStairs(self, n: int) -> int:
        # approach: dp. forwards, decide steps based on previous 1 or 2 vals

        distinct = [0] * n

        # base cases 
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2

        # index 0 = stair 1
        distinct[0] = 1
        distinct[1] = 2

        for i in range(2, n):
            distinct[i] = distinct[i-1] + distinct[i-2]
        
        return distinct[n-1]


        # # base cases
        # if n == 0: return 0
        # if n == 1: return 1
        # if n == 2: return 2

        # dic = [0] * (n+1)
        # dic[0] = 0
        # dic[1] = 1
        # dic[2] = 2

        # for i in range(3, n+1):
        #     dic[i] = dic[i-1] + dic[i-2]

        # return dic[n]