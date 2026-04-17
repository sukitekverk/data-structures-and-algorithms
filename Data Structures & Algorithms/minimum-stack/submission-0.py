class MinStack:

    def __init__(self):
        self.vals = []
        self.minstack = []

        

    def push(self, val: int) -> None:
        self.vals.append(val)
        curr_min = val
        if self.minstack:
            curr_min = min(val, self.minstack[-1])
        self.minstack.append(curr_min)

        
        

    def pop(self) -> None:
        self.vals.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.vals[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        


        
