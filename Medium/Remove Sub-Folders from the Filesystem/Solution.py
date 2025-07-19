class Trie:

    def __init__(self):
        self.folders = {}
    
    def addFolder(self,folderPath):

        f = self.folders        
        paths = folderPath.split("/")[1:]
        for p in paths:
            if '.' in f:
                return 
            if p not in f:
                f[p] = {}
            f = f[p]
        f["."] = "."

    def topFolders(self):
        res = []

        def dfs(currPath,folders):
            if '.' in folders:
                res.append(currPath)
                return 
            
            for p in folders:
                dfs(currPath+"/"+p, folders[p])
            
            return 
        
        
        for p in self.folders:
            dfs("/"+p, self.folders[p])
        
        return res

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        trie  = Trie()

        for f in folder:
            trie.addFolder(f)
        
        return trie.topFolders()
        