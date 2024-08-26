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
        s1 = ""
        s2 = ""

        while (l1):
            s1 += str(l1.val)

            l1 = l1.next

        while (l2):
            s2 += str(l2.val)
            l2 = l2.next

        val = int(s1[::-1]) + int(s2[::-1])
        val = str(str(val)[::-1])
        head = ListNode()
        cur = head
        for c in val:
            cur.next = ListNode(int(c))
            cur = cur.next

        return head.next
    }
};