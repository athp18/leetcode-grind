#include <vector>

class Solution {
public:
    bool canFinish(int numCourses, std::vector<std::vector<int>>& prerequisites) {
        // graph = adjacency list
        std::vector<std::vector<int>> graph(numCourses);
        for (const auto& prereq : prerequisites) {
            graph[prereq[0]].push_back(prereq[1]);
        }

        // keep track
        std::vector<int> visited(numCourses, 0);

        // lets do dfs
        std::function<bool(int)> dfs = [&](int course) -> bool {
            if (visited[course] == -1) return false;
            if (visited[course] == 1) return true;
            visited[course] = -1;
            for (int prereq : graph[course]) {
                if (!dfs(prereq)) return false;
            }
            visited[course] = 1;
            return true;
        };

        // dfs
        for (int course = 0; course < numCourses; ++course) {
            if (!dfs(course)) return false;
        }
        return true;
    }
};
