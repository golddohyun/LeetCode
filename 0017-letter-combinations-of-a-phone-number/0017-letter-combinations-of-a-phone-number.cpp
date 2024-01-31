#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    map<char, string> createAlphabetDictionary() {
        map<char, string> alphabetDict;
        char currentChar = 'a';
        for (char i = '2'; i <= '9'; ++i) {
            int charCount = (i == '7' || i == '9') ? 4 : 3;
            string chars = "";
            for (int j = 0; j < charCount; ++j, ++currentChar) {
                chars += currentChar;
            }
            alphabetDict[i] = chars;
        }
        return alphabetDict;
    }

    void backtrackPerm(const string& digits, int depth, string& current, vector<string>& result, map<char, string>& alphaDict) {
        if (depth == digits.length()) {
            result.push_back(current);
            return;
        }
        char digit = digits[depth];
        for (char ch : alphaDict[digit]) {
            current += ch;
            backtrackPerm(digits, depth + 1, current, result, alphaDict);
            current.pop_back();
        }
    }

    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        map<char, string> alphaDict = createAlphabetDictionary();
        vector<string> result;
        string current;
        backtrackPerm(digits, 0, current, result, alphaDict);
        return result;
    }
};