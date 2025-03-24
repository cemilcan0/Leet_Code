class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        val = []
        for start,end in meetings:
            if not val or val[-1][1] < start:
                val.append([start,end])
            else:
                val[-1][1]= max(val[-1][1],end)

        total_meeting_days = 0
        for start,end in val:
            total_meeting_days += end - start + 1

        return days-total_meeting_days
