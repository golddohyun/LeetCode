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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        ListNode* head = new ListNode();
        ListNode* currentNode = head;
        while(l1 != nullptr || l2 != nullptr) {
            currentNode->next = new ListNode();
            currentNode = currentNode->next;
            int currentSum = carry;
            if(l1 != nullptr) {
                currentSum += l1->val;
            }
            if(l2 != nullptr) {
                currentSum += l2->val;
            }            
            if(currentSum > 9) {
                carry = 1;
                currentSum = currentSum % 10;
            }
            else {
                carry = 0;
            }
            currentNode->val = currentSum;
            
            l1 = l1 != nullptr ? l1->next : nullptr;
            l2 = l2 != nullptr ? l2->next : nullptr;
        }
        
        if(carry == 1) {
            currentNode->next = new ListNode(carry);
        }
               
        return head->next;
    }
};