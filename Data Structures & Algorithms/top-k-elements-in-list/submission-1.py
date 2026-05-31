class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        for num in nums:
            if num in group: group[num]+=1
            else: group[num]=1

        items=list(group.items())
        items.sort(key=lambda x: x[1], reverse=True)

        result=[]
        for i in range (k):
            result.append(items[i][0])

        return result