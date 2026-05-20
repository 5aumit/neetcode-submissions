class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        cmap = dict(zip(nums,[0]*len(nums)))

        for num in nums:
            cmap[num]+=1

            if cmap[num]>1:
                return True
            else:
                continue

        return False
        