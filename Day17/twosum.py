class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''prevMap = {} # val : index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return'''
        l=[ ]
        a=0
        for i in range(len(nums)) : 
            if a==1:
                break
            else:
                for j in range(i+1,len(nums)):
                    if nums[i]+nums[j]==target :
                        l.append(i)
                        l.append(j)
                        a=1
                        break
        return l