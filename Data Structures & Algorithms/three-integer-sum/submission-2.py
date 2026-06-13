class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)

        out = []
        
        for i in range(len(nums)-1):
             l,r = i+1 , len(nums)-1

             while l<r:
                if (nums[i] + nums[l] + nums[r] == 0) and ([nums[i], nums[l], nums[r]] not in out):
                    out.append([nums[i], nums[l], nums[r]])
                    l += 1

                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                    continue

                else:
                    r -= 1
                    continue

        return out
                