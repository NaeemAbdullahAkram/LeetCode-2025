/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if(!head || left == right) return head;

        ListNode* dum = new ListNode(0);
        dum->next = head;
        ListNode* pre = dum;

        for(int i= 1; i<left; i++){
            pre = pre->next;
        }

        ListNode* start = pre->next;
        ListNode* then = start->next;

        for(int i=0; i<right-left; i++){
            start->next = then->next;
            then->next = pre->next;
            pre->next = then;
            then = start->next;
        }
        return dum->next;
    }
};