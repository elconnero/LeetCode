#include <string>
#include <unordered_set>
using namespace std;

class Solution {
public:
    string reverseVowels(string s) {
        
        if (s.length() == 1) return s;

        int left = 0, right = s.length() - 1;
        unordered_set<char> vowels = {'a','e','i','o','u','A','E','I','O','U'};

        while (left < right) {

            if (vowels.count(s[left]) && vowels.count(s[right])) {
                swap(s[left], s[right]);
                left++;
                right--;
            }
            else if (!vowels.count(s[left])) left++;
            else if (!vowels.count(s[right])) right--;
        }
        return s;
    }
};