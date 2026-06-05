#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {

        sort(nums.begin(), nums.end());  // sort in place
        int left = 0;
        int right = 1;

        if (nums.size() == 1) return false;

        while (right < nums.size()) {
            if (nums[left] == nums[right]) return true;
            left++;
            right++;
        }
        return false;
    }
};

int main() {

    Solution sol;

    vector<vector<int>> testCases = {
        {1, 2, 3, 1},           // expected: true
        {1, 2, 3, 4},           // expected: false
        {1, 1, 1, 3, 3, 4, 3, 2, 4, 2}  // expected: true
    };

    for (int i = 0; i < testCases.size(); i++) {
        cout << (sol.containsDuplicate(testCases[i]) ? "True" : "False") << endl;
    }

    return 0;
}