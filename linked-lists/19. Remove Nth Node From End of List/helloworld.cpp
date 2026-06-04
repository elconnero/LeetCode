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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        if (!head) return nullptr;

        ListNode* dummy = new ListNode(0);
        ListNode* left = dummy;
        ListNode* right = dummy;
        dummy->next = head;

        for (int i = 0; i < n + 1; i++) right = right->next;

        while (right != nullptr) {
            left = left->next;
            right = right->next;
        }

        left->next = left->next->next;

        return dummy->next;
    }
};

int main() {

    // Test 1: remove 2nd node from end of [1,2,3,4,5]
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);

    Solution sol;
    ListNode* result = sol.removeNthFromEnd(head, 2);

    ListNode* curr = result;
    while (curr != nullptr) {
        cout << curr->val << " -> ";
        curr = curr->next;
    }
    cout << "None" << endl;

    // Test 2: remove head
    ListNode* head2 = new ListNode(1);
    head2->next = new ListNode(2);

    ListNode* result2 = sol.removeNthFromEnd(head2, 2);

    curr = result2;
    while (curr != nullptr) {
        cout << curr->val << " -> ";
        curr = curr->next;
    }
    cout << "None" << endl;

    // Test 3: single node
    ListNode* head3 = new ListNode(1);
    ListNode* result3 = sol.removeNthFromEnd(head3, 1);
    cout << (result3 == nullptr ? "None" : "Not None") << endl;

    return 0;
}