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
        L1=[]
        L2=[]
        res=[]
        cf=0
        n=l1
        while(n!=None):
            L1.append(n.val)
            n=n.next
        n=l2
        while(n!=None):
            L2.append(l2.val)
            n=n.next
        Max=0
        if len(L1)>len(L2):
            Max=[len(L2),len(L1),1]
        else:
            Max=[len(L1),len(L2),2]

        for i in range(Max[1]):
            if i+1>Max[0]:
                res.append((L1[i]+L2[i]+cf)%10)
                cf=(int)((L1[i]+L2[i]+cf)/10)
            elif Max[2]==1:
                res.append((L1[i]+cf)%10)
                cf=(int)((L1[i]+cf)/10)
            elif Max[2]==2:
                res.append((L2[i]+cf)%10)
                cf=(int)((L2[i]+cf)/10)
        n=ListNode(0)
        for i in range(len(res))[::-1]:
            p=ListNode(res[i])
            n.next,p.next=p,n.next
        return n.next
# 报错了。。。
