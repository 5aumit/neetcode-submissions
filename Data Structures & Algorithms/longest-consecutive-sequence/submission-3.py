class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0

        numset = set(nums)
        # l = 0
        longest = 0

        for num in nums:
            l=0
            while num+l in nums:
                l+=1
                if l>=longest:
                    longest=l

        return longest