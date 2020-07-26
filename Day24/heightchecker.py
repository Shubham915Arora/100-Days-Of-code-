class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        c=0
        mini=0
        x=heights.copy()
        for i  in range(0,len(heights)) :
            for j in range(i+1,len(heights)):
                if heights[i]>heights[j]:
                    
                    mini=heights[j]
                    heights[j]=heights[i]
                    heights[i]=mini
                    #c+=1
        #print(heights)
        
        for k in range(0,len(x)):
            if x[k]!=heights[k]:
                c+=1
        return c