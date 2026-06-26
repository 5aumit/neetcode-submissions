class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r = 0,len(nums)-1

        while l<=r:

            midIndex = (l+r)//2
            mid = nums[midIndex]

            if target>mid:
                l=midIndex+1
            elif target<mid:
                r=midIndex-1
            elif target==mid:
                return midIndex

        return -1
