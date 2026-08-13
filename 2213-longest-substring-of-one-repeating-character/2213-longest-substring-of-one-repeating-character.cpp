class Solution {
public:
struct Node {
        int l, r;
        int lmax, rmax, mx;
    };

    vector<Node> tree;
    string s;

    void build(int node, int l, int r) {

        tree[node].l = l;
        tree[node].r = r;

        if (l == r) {
            tree[node].lmax = 1;
            tree[node].rmax = 1;
            tree[node].mx = 1;
            return;
        }

        int mid = (l + r) / 2;

        build(node * 2, l, mid);
        build(node * 2 + 1, mid + 1, r);

        merge(node);
    }

    void merge(int node) {

        Node &cur = tree[node];
        Node &left = tree[node * 2];
        Node &right = tree[node * 2 + 1];

        cur.lmax = left.lmax;
        cur.rmax = right.rmax;

        cur.mx = max(left.mx, right.mx);

        // Check if the two parts can be joined
        if (s[left.r] == s[right.l]) {

            int leftLength = left.r - left.l + 1;
            int rightLength = right.r - right.l + 1;

            // Entire left part has same character
            if (left.lmax == leftLength)
                cur.lmax = left.lmax + right.lmax;

            // Entire right part has same character
            if (right.rmax == rightLength)
                cur.rmax = left.rmax + right.rmax;

            // Join suffix of left + prefix of right
            cur.mx = max(cur.mx, left.rmax + right.lmax);
        }
    }

    void update(int node, int pos, char ch) {

        int l = tree[node].l;
        int r = tree[node].r;

        if (l == r) {
            s[pos] = ch;
            return;
        }

        int mid = (l + r) / 2;

        if (pos <= mid)
            update(node * 2, pos, ch);
        else
            update(node * 2 + 1, pos, ch);

        merge(node);
    }
    vector<int> longestRepeating(string s, string queryCharacters, vector<int>& queryIndices) {
        this->s = s;

        int n = s.size();

        tree.resize(4 * n);

        build(1, 0, n - 1);

        vector<int> ans;

        for (int i = 0; i < queryIndices.size(); i++) {

            int pos = queryIndices[i];
            char ch = queryCharacters[i];

            update(1, pos, ch);

            ans.push_back(tree[1].mx);
        }

        return ans;
        
    }
};