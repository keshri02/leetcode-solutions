class Solution {
public:
    bool winnerSquareGame(int n) 
    {
        /*if (n<0)
        return false;
        int root=sqrt(n);
        return ((long long)root * root == n);*/
        vector<bool> dp(n + 1, false);

        for (int i = 1; i <= n; i++) {

            // Try every perfect square
            for (int j = 1; j * j <= i; j++) {

                int square = j * j;

                // If removing this square makes
                // the opponent lose, I win
                if (dp[i - square] == false) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[n];
    }
};
