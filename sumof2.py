class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=[]
        c=0
        k=0
        for i in range(0,len(numbers)):
            for j in range(0,len(numbers)):
                if i==j:
                    continue
                else :
                    k=numbers[i]+numbers[j]
                if k==target:
                    return(i+1,j+1)
           
            
        return l