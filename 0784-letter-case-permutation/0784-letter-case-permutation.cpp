#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

class Solution {
public:
    void swapcase(std::string &data, int idx) {
        if (islower(data[idx])) {
            data[idx] = toupper(data[idx]);
        } else {
            data[idx] = tolower(data[idx]);
        }
    }

    void permute(std::string &data, int i, int length, std::unordered_set<std::string> &result) {
        if (i == length) {
            result.insert(data);
        } else {
            // Include the current character as is
            permute(data, i + 1, length, result);

            if (isalpha(data[i])) {
                swapcase(data, i);
                permute(data, i + 1, length, result);
                swapcase(data, i); // Swap back
            }
        }
    }

    std::vector<std::string> letterCasePermutation(std::string s) {
        std::vector<std::string> ans;
        std::unordered_set<std::string> resultSet;

        if (s.length() == 1) {
            if (isalpha(s[0])) {
                std::string upperCase(1, toupper(s[0]));
                std::string lowerCase(1, tolower(s[0]));
                return {upperCase, lowerCase};
            }
        }

        permute(s, 0, s.length(), resultSet);
        ans.assign(resultSet.begin(), resultSet.end());
        return ans;
    }
};
