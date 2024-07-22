bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    if (matrixSize == 0 || matrixColSize[0] == 0) {
        return false;
    }

    int m = matrixSize;
    int n = matrixColSize[0];
    int l = 0, r = m * n - 1;

    while (l <= r) {
        int mid = l + (r - l) / 2;
        int mid_value = matrix[mid / n][mid % n];

        if (mid_value == target) {
            return true;
        } else if (mid_value < target) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }

    return false;
}
