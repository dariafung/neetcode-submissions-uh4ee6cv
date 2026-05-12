class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> matrix(n, vector<int>(n, 0));

        int top = 0, bottom = n - 1;
        int left = 0, right = n - 1;
        int num = 1;

        while (top <= bottom && left <= right){
            for(int j = left; j <= right; j++){
                matrix[top][j] = num++;
            }
            top++;

            for(int j = top; j <= bottom; j++){
                matrix[j][right] = num++;
            }
            right--;

            for(int j = right; j >= left; j--){
                matrix[bottom][j] = num++;
            }
            bottom--;

            for(int j = bottom; j >= top; j--){
                matrix[j][left] = num++;
            }
            left++;
        }

        return matrix;
    }
};