#include <bits/stdc++.h>
typedef long long ll;
#define endl "\n";
#define IOS ios::sync_with_stdio(0); cin.tie(0); 
using namespace std;

// Problem: https://leetcode.com/problems/longest-common-prefix/solution/

void vertical_scanning(int n){
    // Time complexity: O(S), S is the sum of all characters in strings. If you have n same strings with m characters. You have to perform n*m = S comparisons. Best case time complexity: O(n*minlen). Space complexity: O(1).

    vector<string> strings(n);
    int minlen = INT32_MAX;
    string temp;
    for (int i = 0; i < n; i++){
        cin>>temp;
        minlen = min(minlen, (int) temp.size());
        strings[i] = temp;
    }

    string pref = "";
    for (int i = 0; i<minlen; i++){
        char chr = strings[0][i];
        for (string s: strings){
            if (s[i] != chr){
                cout<<pref<<endl;
                exit(0);
            }
        }
        pref += string(1, chr);
        
    } 
    cout<<pref<<endl;
}

void horizontal_scanning(int n){
    // LCP(S1...Sn) = LCP((LCP(LCP..LCP(S1, S2), S3), S4).., Sn). Time complexity: O(S), S is the sum of all characters in strings.

    vector<string> strings(n);
    for (int i = 0; i<n; i++) cin>>strings[i];

    string pref = strings[0];
    for (int i = 1; i<n; i++){
        int j = 0;
        for (j; j<min(pref.size(), strings[i].size()); j++){
            if (pref[j] != strings[i][j]){
                break;
            }
        }
        if (j==0){
            cout<<""<<endl;
            exit(0);
        }
        pref = pref.substr(0, j);
    }
    cout<<pref;
}

string commonPrefix(string lcp, string rcp){
    int minlen = min(lcp.size(), rcp.size());
    int i = 0;
    for (; i<minlen; i++){
        if (lcp[i]!=rcp[i]) break;
    }
    return lcp.substr(0, i);
};

string longestCommonPrefix(vector<string> strings, int l, int r){
    if (l == r) return strings[l];
    else{
        int mid = (l + r)/2;
        string lcp = longestCommonPrefix(strings, l, mid);
        string rcp = longestCommonPrefix(strings, mid+1, r);
        return commonPrefix(lcp, rcp);
    }
}

void divide_and_conquer(int n){
    /* Key intuition to use divide and conquer comes from the associative property of the LCP function.

    LCP(s1...sn) = LCP(LCP(s1...sk), LCP(sk+1...sn))

    O(S) time complexity. Where S is the number of characters = n*m.
    Time complexity is 2.T(n/2) + O(m) = O(S).
    Space complexity is O(m log N). There is a memory overhead since we store recursive calls in the execution stack. There are logn recursive calls, each store need m space to store the result.
    */

    vector<string> strings(n);
    for (int i = 0; i<n; i++) cin>>strings[i];
    cout<<longestCommonPrefix(strings, 0, strings.size() - 1);

}

int main(){
    int n;
    cin>>n;
    if (n==0) return 0;
    // vertical_scanning(n);
    // horizontal_scanning(n);
    divide_and_conquer(n);
}