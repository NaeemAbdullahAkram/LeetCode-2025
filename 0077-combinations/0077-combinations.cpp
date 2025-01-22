class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> ans;
        int total_combinations = 1 << n; // 2^n combinations
        
        for (int i = 0; i < total_combinations; i++) {
            vector<int> combination;
            for (int j = 0; j < n; j++) {
                // Check if the j-th bit is set in i
                if (i & (1 << j)) {
                    combination.push_back(j + 1);
                }
            }
            // If the combination has exactly k elements, add it to the answer
            if (combination.size() == k) {
                ans.push_back(combination);
            }
        }
        
        return ans;
    }
};