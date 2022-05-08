// 2022-05-08 16:58:39
// Runtime 88ms(5.5%)
// Memory 8.4mb(72.1%)

/**
 * ??这么慢怎会如此
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> reversePrint(ListNode* head) {
        vector<int> ret;
        while(head) {
            ret.insert(ret.begin(), head->val);
            head = head->next;
        }
        return ret;
    }
};
