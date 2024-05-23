class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        start = 0
        end = len(people)-1
        boats = 0
        while start <= end:
            if people[end] == limit:
                boats +=1
                end -=1
            elif people[end] < limit:
                if people[end] + people[start] <= limit:
                    boats +=1
                    end -=1
                    start+=1
                else:
                    boats+=1
                    end -=1
        return boats
                



        
        