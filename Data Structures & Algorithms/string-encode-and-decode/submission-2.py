class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            out = 'empty'
        else:
            out = '<word>'.join([f'{s}' for s in strs])
        return out

    def decode(self, s: str) -> List[str]:
        if s=='empty':
            out=[]
        else:
            out = s.split('<word>')
        return out

