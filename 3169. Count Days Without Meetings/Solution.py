    class Solution:
        def countDays(self, days: int, meetings: List[List[int]]) -> int:
            # visited = set()
            # for start, end in meetings:
            #     visited.update(range(start, end+1))
            # return days - len(visited)

            new = []
            if len(meetings) == 1:
                new = meetings

            else:
                meetings.sort()
                new.append(meetings[0])

                for start, end in meetings[1:]:
                    last_start, last_end = new[-1]

                    if start <= last_end:
                        new[-1][1] = max(last_end, end)
                    else:
                        new.append([start, end])
                    
            count = 0
            for i in range(len(new)-1):
                diff = (new[i+1][0] - new[i][1]) - 1 
                count += diff
            
            min_val = min([min(meet) for meet in meetings])
            max_val = max([max(meet) for meet in meetings])

            return count + (days - max_val) + (min_val - 1)
