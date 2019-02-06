
// Definition for singly-linked list.
public class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int cf=0;
        ListNode res=new ListNode(0);
        ListNode p=res;
        while(l1!=null || l2!=null || cf==1){
            int val=(l1!=null?l1.val:0)+(l2!=null?l2.val:0)+cf;
            p.next=new ListNode(val%10);
            cf=(int)(val/10);
            if(l1!=null)l1=l1.next;
            if(l2!=null)l2=l2.next;
            p=p.next;
        }
        return res.next;
    }
}