class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        freq = [[] for i in range(len(nums)+1)]
        out=[]

        for num in nums:
            if num in counts.keys():
                counts[num]+=1
            else:
                counts[num]=1

        print(counts)

        for num,count in counts.items():
            freq[count].append(num)

        print(freq)

        for i in range(len(freq)-1, 0 ,-1):
            if len(freq[i])>0:
                for num in freq[i]:
                    out.append(num)
                    if len(out)==k:
                        return out


        

        