class Trie:
    def __init__(self):
        self.subFolders={}
        self.serial = ""
    
    def setupFolders(self,path):

        f = self.subFolders

        for folder in path:
            if folder not in f:
                f[folder] = Trie()
            
            f = f[folder].subFolders
        
        



class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:

        root = Trie()
        res = []
        for path in paths:
            root.setupFolders(path)
        

        count = defaultdict(int)
        def hash(folder):

            if not folder.subFolders:
                return 
            
            files = []

            for sF, f in folder.subFolders.items():
                hash(f)
                files.append(sF + '(' + f.serial + ')')
            
            files.sort()

            folder.serial = "".join(files)

            count[folder.serial] += 1
        

        hash(root)


        sol = []

        def dfs(folder):

            if count[folder.serial] > 1:
                return 
            
            if sol:
                res.append(sol[:])
            

            for sf in folder.subFolders:
                sol.append(sf)
                dfs(folder.subFolders[sf])
                sol.pop()
        

        dfs(root)
        return res



            
            
        