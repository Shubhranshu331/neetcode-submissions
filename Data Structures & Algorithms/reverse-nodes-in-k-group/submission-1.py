# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==1:
            return head
        dummy=ListNode(0)
        dummy.next=head
        group_prev = dummy
        while True:
            kth = self.getKthNode(group_prev,k)
            if not kth:
                break
            group_next=kth.next
            prev, curr = kth.next, group_prev.next
            while curr!=group_next:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            temp=group_prev.next
            group_prev.next=kth
            group_prev=temp
        return dummy.next
    def getKthNode(self,curr,k):
        while curr and k>0:
            curr= curr.next
            k-=1
        return curr                  