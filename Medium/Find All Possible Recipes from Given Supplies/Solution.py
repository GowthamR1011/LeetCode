class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        rec_dict = {}

        for i in range(len(recipes)):
            rec_dict[recipes[i]] = ingredients[i]

        
        supplies = set(supplies)
        seen = set()

        def dfs(pro):
            
            if pro in supplies: return True
            
            if pro not in rec_dict or pro in seen: return False
            
            seen.add(pro)
            
            for ing in rec_dict[pro]:
                if not dfs(ing):
                    return False
            
            
            supplies.add(pro)

            return True
        
        res = []
        for rec in recipes:
            if dfs(rec):
                res.append(rec)
        
        return res
                

