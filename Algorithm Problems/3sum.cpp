#include <bits/stdc++.h>
#include <unordered_set>
typedef long long ll;
#define endl "\n";
#define IOS ios::sync_with_stdio(0); cin.tie(0); 
using namespace std;

void twoPointer(int n){
    vector<int> nums(n, 0);
    for(int i = 0; i<n; i++) cin>>nums[i];

    sort(nums.begin(), nums.end());

    vector<vector<int>> ans;
    unordered_set<int> seen;
    for (int i = 0; i<n-1; i++){
        int l = i+1, r = n-1;
        int a = nums[i];
        
        if (seen.find(a)!=seen.end()) continue;
        else seen.insert(a);

        while (l<r){
            int b = nums[l], c = nums[r];
            int s = a + b + c;
            
            if (s == 0) {
                ans.push_back({a, b, c});
                l++;
                r--;
            }
            else if (s > 0){
                r--;
            } 
            else l++;
        }
    }

    for (int i = 0; i < ans.size(); i++){
        for (int j = 0; j < ans[i].size(); j++){
            cout<<ans[i][j]<<" ";
        }
        cout<<endl;
    }
}


int main(){
    int n; cin>>n;
    if (n==0) return 0;
    twoPointer(n);
}

