class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result=[]
        for i in range(1,n+1) :
            if (len(target)>0):
                if i in target :
                    result.append("Push")
                    target.remove(i)
                else :
                    result.append("Push")
                    result.append("Pop")
            
            else : 
                break
                
        return result
            