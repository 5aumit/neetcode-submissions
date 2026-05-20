class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        cmap = {}
        out = []

        for i,s in enumerate(strs):
            sset = ''.join(sorted(s))
            if sset in cmap.keys():
                cmap[sset].append(s)
            else:
                cmap[sset] = [s]

        for k,v in cmap.items():
            out.append(v)

        return out
