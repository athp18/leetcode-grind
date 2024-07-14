class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>(); //array list
        if (matrix == null || matrix.length == 0) {
            return result;
        }
        //four corners
        int l = 0;
        int r = matrix[0].length-1;
        int t = 0;
        int b = matrix.length-1;

        while (l <= r && t <= b) {
            for (int i = l; i <= r; i++) {
                result.add(matrix[t][i]);
            }
            t++;
            for (int i = t; i <= b; i++) {
                result.add(matrix[i][r]);
            }
            r--;
            if (t <= b) {
                for (int i = r; i >= l; i--) {
                    result.add(matrix[b][i]);
                }
                b--;
            }
            if (l <= r) {
                for (int i = b; i >= t; i--) {
                    result.add(matrix[i][l]);
                }
                l++;
            }
        }
        return result;
    }
}
