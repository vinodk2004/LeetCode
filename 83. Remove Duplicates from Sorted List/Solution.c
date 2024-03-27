/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    if(head == NULL || head->next == NULL){
        return head;
    }
    struct ListNode *prev = head;
    struct ListNode *curr = head->next;
    while(curr != NULL){
        if (curr->val == prev->val){
            prev->next = curr->next;
        }
        else{
            prev = prev->next;
        }
        curr = curr->next;
    }
    return head;
}