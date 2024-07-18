class Solution {
public:
    bool backspaceCompare(std::string s, std::string t) {
        std::string a = processString(s);
        std::string b = processString(t);
        return a == b;
    }

private:
    std::string processString(const std::string &str) { //helper func 
        std::stack<char> stck;
        for (char c : str) {
            if (c == '#') {
                if (!stck.empty()) {
                    stck.pop();
                }
            } else {
                stck.push(c);
            }
        }

        std::string result;
        while (!stck.empty()) {
            result += stck.top();
            stck.pop();
        }
        std::reverse(result.begin(), result.end());  //reverse
        return result;
    }
};
