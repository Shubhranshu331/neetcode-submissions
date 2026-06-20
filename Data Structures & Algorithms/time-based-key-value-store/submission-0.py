from collections import defaultdict
from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.ktv=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ktv[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ktv:
            return ""
        timestamps_values=self.ktv[key]
        i=bisect_right(timestamps_values,(timestamp,chr(127)))
        if i ==0:
            return ""
        return timestamps_values[i-1][1]
