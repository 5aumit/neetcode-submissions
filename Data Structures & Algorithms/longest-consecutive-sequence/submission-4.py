class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0

        numset = set(nums)
        longest = 0

        for num in numset:
            if num-1 not in numset: #Start of new sequence
                l=1
                while num+l in nums:
                    l+=1
                longest = max(l,longest)

        return longest