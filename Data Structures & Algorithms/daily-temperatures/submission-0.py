class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #if smaller put on top
        #if bigger take of the top
        #The numer you take off coreepond to that days count

        stack = []
        res = [0]* len(temperatures)
        for i, n in enumerate(temperatures):
            while stack and stack [-1][1]<n:
                res[stack [-1][0]] = i-stack [-1][0]
                stack.pop()
            stack.append((i,n))
        return res

        