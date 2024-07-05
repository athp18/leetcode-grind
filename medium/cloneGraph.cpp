/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

// i didn't think i hated graphs til i solved this problem
// the basic algorithm is a breadth first search

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;
        
        unordered_map<Node*, Node*> cloneMap;
        
        // Queue for BFS
        queue<Node*> q;
        q.push(node);
        cloneMap[node] = new Node(node->val);
        
        while (!q.empty()) {
            Node* curr = q.front();
            q.pop();
            for (Node* neighbor : curr->neighbors) {
                if (cloneMap.find(neighbor) == cloneMap.end()) {
                    cloneMap[neighbor] = new Node(neighbor->val);
                    q.push(neighbor);
                }
                cloneMap[curr]->neighbors.push_back(cloneMap[neighbor]);
            }
        }
        return cloneMap[node];
    }
};
