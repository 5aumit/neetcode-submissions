class MinStack:

    def __init__(self):
        self.stack = []
        self.minlist = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minlist or val<=self.minlist[-1]: # If minlist is empty and val is smaller
            self.minlist.append(val) 
        

    def pop(self) -> None:
        out = self.stack[-1]
        self.stack.pop()

        if out==self.minlist[-1]: # If min gets popped
            self.minlist.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:

        return self.minlist[-1]
        
