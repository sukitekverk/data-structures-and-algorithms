class TimeMap:

    def __init__(self):
        self.map={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key]= []
        self.map[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        values =self.map[key]

        ##binary search
        res = ""
        l= 0
        r = len(values) -1
        while r>=l:
            mid = (r+l)//2
            if values[mid][1]<= timestamp:
                res = values[mid][0]
                l= mid+1
            else:
                r= mid-1
        return res

        
