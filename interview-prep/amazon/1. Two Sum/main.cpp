#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int, int> seen;  // value -> index

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            if (seen.count(complement)) {
                return {seen[complement], i};  // found the pair
            }
            seen[nums[i]] = i;  // store value -> index
        }
        return {};  // no solution found
    }
};

int main() {

    Solution sol;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;

    vector<int> result = sol.twoSum(nums, target);

    cout << "[" << result[0] << ", " << result[1] << "]" << endl;
    // expected: [0, 1]

    return 0;
}