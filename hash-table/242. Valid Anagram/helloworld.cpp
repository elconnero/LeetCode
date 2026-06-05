#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {

        if (s.length() != t.length()) return false;

        unordered_map<char, int> seen;

        // count characters in s
        for (char c : s) {
            if (seen.count(c)) seen[c]++;
            else seen[c] = 1;
        }

        // check characters in t
        for (char c : t) {
            if (!seen.count(c)) return false;
            seen[c]--;
            if (seen[c] < 0) return false;
        }
        return true;
    }
};

int main() {

    Solution sol;

    vector<string> test_case_s = {"anagram", "rat", "car"};
    vector<string> test_case_t = {"nagaram", "car", "rac"};

    for (int i = 0; i < test_case_s.size(); i++) {
        cout << (sol.isAnagram(test_case_s[i], test_case_t[i]) ? "True" : "False") << endl;
    }

    return 0;
}