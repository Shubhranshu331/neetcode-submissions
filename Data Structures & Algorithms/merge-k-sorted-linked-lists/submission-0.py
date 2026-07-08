# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        heap=[]
        count=0
        for l in lists:
            if l:
                heapq.heappush(heap,(l.val, count, l))
                count+=1
        while heap:
            val, _, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                count+=1
                heapq.heappush(heap, (node.next.val, count, node.next))
        return dummy.next