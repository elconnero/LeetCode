#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        int carry = 0;

        while (l1 != nullptr || l2 != nullptr || carry) {

            int val1 = l1 ? l1->val : 0;  // get val or 0 if list is exhausted
            int val2 = l2 ? l2->val : 0;

            int total = val1 + val2 + carry;
            carry = total / 10;            // carry the tens digit
            curr->next = new ListNode(total % 10);  // store the ones digit

            curr = curr->next;
            if (l1) l1 = l1->next;
            if (l2) l2 = l2->next;
        }

        return dummy->next;
    }
};

int main() {

    // l1 = [2,4,3] l2 = [5,6,4] expected = [7,0,8] (342 + 465 = 807)
    ListNode* l1 = new ListNode(2);
    l1->next = new ListNode(4);
    l1->next->next = new ListNode(3);

    ListNode* l2 = new ListNode(5);
    l2->next = new ListNode(6);
    l2->next->next = new ListNode(4);

    Solution sol;
    ListNode* result = sol.addTwoNumbers(l1, l2);

    ListNode* curr = result;
    while (curr != nullptr) {
        cout << curr->val << " -> ";
        curr = curr->next;
    }
    cout << "None" << endl;
    // expected: 7 -> 0 -> 8 -> None

    return 0;
}