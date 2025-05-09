class TimeMap:

    def __init__(self):
        
        self.storage = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.storage:
            self.storage[key] = [(timestamp,value)]
        else:
            self.storage[key].append((timestamp,value))
    

    def get(self, key: str, timestamp: int) -> str:
        
        res = ""
        if key not in self.storage:
            return res
        
        search = self.storage[key]
        
        l,h = 0, len(search) - 1

        while l<=h:

            m = (l + h) // 2

            if search[m][0] <= timestamp:
                res = search[m][1]
                l = m + 1
            else:
                h = m - 1
        
        return res
