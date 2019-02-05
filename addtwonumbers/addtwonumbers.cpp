
// Definition for singly-linked list.
#ifndef NULL
#define NULL 0
#endif
struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* res=new ListNode(0);
        ListNode* pointer=res;
        int cf=0;
        while(l1 or l2 or cf){
            int val=(l1?l1->val:0)+(l2?l2->val:0)+cf;
            pointer->next=new ListNode(val%10);
            cf=int(val/10);
            if(l1)l1=l1->next;//这里两行容易出错：
            if(l2)l2=l2->next;//假如l1,l2均已经为NULL,但是cf仍可进位,此时操作l1->next;会报错
            pointer=pointer->next;
        }
        return res->next;
        
    }
};