class Solution {
public:
    int uniquePaths(int m, int n) {
        /*
        so here is the algorithm:
        its a dp problem. so essentially, we track the number of "ways" to reach the end point (down or up)
        so (len(n[0], len(n)) is the final point. 
        there's 0 ways to reach that point. 
        for the entire last row, theres only 1 way to reach the 
        end point (go right)
        for the entire last column, there's only way 1 way to reach the end point (go down)
        at the coordiinate (len(n[0], len(n-1))), there's two ways: go right and then down, or go down and then right. the pattern you start to notice is that each point (a, b) has a number of possiblities equal to the
        possibilities as (a-1, b) + the possibilities at (a, b-1).
        following that logic, the "start" point will be a sum of the total possiblities
        QED or some shit idk

        */
        std::vector<int> row(n, 1);
        for (int i = 0; i < m -1; i++) {
            std::vector<int> new_row(n, 1);
            for (int j = n - 2; j >= 0; j--) {
                new_row[j] = new_row[j+1] + row[j];
            }
            row = new_row;
        }
        return row[0];
    }
};
