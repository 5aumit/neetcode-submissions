class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        cmap = {}

        for i,num in enumerate(nums):

            if target-num in cmap.keys() and cmap[target-num]!=i:
                return[ min(i , cmap[target-num]) , max(i , cmap[target-num])]
            else:
                cmap[num] = i
                continue