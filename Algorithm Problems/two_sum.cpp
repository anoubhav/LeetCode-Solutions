#include <bits/stdc++.h>
typedef long long ll;
#define endl "\n";
#define IOS ios::sync_with_stdio(0); cin.tie(0); 
using namespace std;

vector<int> solve(int n, int target){
    vector <int> nums;
    for (int i = 0; i< n; i++){
        int temp;
        cin>>temp;
        nums.push_back(temp);
    }

    unordered_map<int, int> d;
    for (int i = 0; i<n; i++){
        if (d.find(target - nums[i])!=d.end()){
            return {d[target - nums[i]], i};
        }
        d[nums[i]] = i;
    }
    return {-1, -1};
}
int main(){
    int target;
    int n;
    vector<int> ans;
    cin>>n>>target;
    ans = solve(n, target);
    for (auto x: ans)cout<<x<<" ";
    return 0;
}