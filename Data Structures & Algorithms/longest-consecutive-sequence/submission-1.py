class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums)==0:
            return 0
        
        nums = (sorted(nums))
        maxl=1
        l = 1

        for i,num in enumerate(nums):

            if (i==0) or (num==nums[i-1]):
                continue
            
            if num == nums[i-1]+1:
                l+=1
            else:
                l=1

            if l>maxl:
                maxl=l

            # print(num,l,maxl)

        return maxl