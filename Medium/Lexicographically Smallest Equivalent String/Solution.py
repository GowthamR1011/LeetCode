class UnionFind:

    def __init__(self):
        self.parents = [i for i in range(26)]

    def find(self,x):


        if self.parents[x] == x:
            return x
        
        return self.find(self.parents[x])

    def union(self,x,y):
        
        parent_x = self.find(x)
        parent_y = self.find(y)

        if (parent_x == parent_y):
            return
        
        elif parent_x < parent_y:
            self.parents[parent_y] = parent_x
        else:
            self.parents[parent_x] = parent_y


        
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        UF = UnionFind()

        n = len(s1)

        for i in range(n):
            UF.union(ord(s1[i]) - ord('a') , ord(s2[i]) - ord('a'))
        
        res = ""

        for ch in baseStr:
            res += chr(ord('a') + UF.find(ord(ch) - ord('a')))
        
        return res