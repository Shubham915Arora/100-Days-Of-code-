class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx=-1
        for i in range(0,len(nums)):
            if nums[i]>=target:
                idx=i
                break 
                
        if idx==-1:
            return len(nums)
        else :
            return idx 