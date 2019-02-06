# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #init
        res=ListNode(0)
        p=res
        cf=0
        while(l1 or l2 or cf):
            val=((l1 and l1.val or 0)+(l2 and l2.val or 0)+cf)#and与or的整型数应用
            p.next=ListNode(val%10)
            cf=(int)(val/10)
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
            p=p.next
        return res.next
