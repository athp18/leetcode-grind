// since i hate my life
class Solution {
public:
    std::string encode(const std::vector<std::string>& strs) {
        std::string result;
        for (const auto& s : strs) {
            result += std::to_string(s.length()) + "#" + s;
        }
        return result;
    }

    std::vector<std::string> decode(const std::string& s) {
        std::vector<std::string> result;
        size_t i = 0;
        while (i < s.length()) {
            size_t j = i;
            while (s[j] != '#') {
                j++;
            }
            int length = std::stoi(s.substr(i, j - i));
            result.push_back(s.substr(j + 1, length));
            i = j + 1 + length;
        }
        return result;
    }
};
