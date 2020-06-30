#include <bits/stdc++.h>
typedef long long ll;
#define endl "\n";
#define IOS ios::sync_with_stdio(0); cin.tie(0); 
using namespace std;

int brute(vector <int> containers){
    // O(N^2) solution
    int maxwater = 0;
    for (int i = 0; i< containers.size(); i++){
        for (int j = i + 1; j<containers.size(); j++){
            maxwater = max(maxwater, (j-i)*(min(containers[i], containers[j])));
        }
    }
    return maxwater;
}

int twoPointer(vector <int> containers){
    // We starts with the widest container, l = 0 and r = n - 1. Let's say the left one is shorter: h[l] < h[r]. Then, this is already the largest container the left one can possibly form. There's no need to consider it again. Therefore, we just throw it away and start again with l = 1 and r = n -1.
    
    int i = 0, j = containers.size()-1;
    int maxarea = 0;
    int area = 0;
    while (i!=j){
        area = (j-i)*(min(containers[i], containers[j]));
        maxarea = max(maxarea, area);
        if (containers[i]>containers[j]) j--;
        else i++;
    }
    return maxarea;
}

int main(){
    int n;
    cin>>n;
    vector<int> containers(n);
    for (int i = 0; i < n; i++) cin>>containers[i];

    // cout<<brute(containers);
    cout<<twoPointer(containers);
}