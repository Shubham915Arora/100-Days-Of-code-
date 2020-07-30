class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dct={}
        for i in paths:
            dct[i[0]]=i[1]
            
        for i in dct.values():
            if i not in dct.keys():
                return i