#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {

        int left = 1;
        int right = *max_element(piles.begin(), piles.end());
        int res = right;

        while (left <= right) {
            int k = (left + right) / 2;
            long long hours = 0;

            for (int p : piles) hours += ceil((double)p / k);

            if (hours <= h) {
                res = min(res, k);
                right = k - 1;
            } else {
                left = k + 1;
            }
        }
        return res;
    }
};

int main() {

    Solution sol;

    vector<int> piles1 = {3, 6, 7, 11};
    cout << sol.minEatingSpeed(piles1, 8) << endl;  // expected: 4

    vector<int> piles2 = {30, 11, 23, 4, 20};
    cout << sol.minEatingSpeed(piles2, 5) << endl;  // expected: 30

    vector<int> piles3 = {30, 11, 23, 4, 20};
    cout << sol.minEatingSpeed(piles3, 6) << endl;  // expected: 23

    return 0;
}