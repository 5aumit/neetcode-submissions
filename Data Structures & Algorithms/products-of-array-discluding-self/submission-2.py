class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lprod = [None]*len(nums)
        rprod = [None]*len(nums)

        for i in range(0,len(nums)):
            if i==0:
                lprod[i]=1
            else:
                lprod[i] = lprod[i-1]*nums[i-1]
        
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                rprod[i]=1
            else:
                rprod[i] = rprod[i+1]*nums[i+1]

        # print(lprod, rprod)

        return [lprod[i]*rprod[i] for i in range(len(nums))]

        