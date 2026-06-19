class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        ps = dict(zip(position,speed))
        position = sorted(position)

        timeleft = [(target-p)/ps[p] for p in position]

        fleets = []

        for i,t in enumerate(timeleft):
            
            while fleets and t>=fleets[-1]:
                fleets.pop()

            fleets.append(t)

        return len(fleets)




        