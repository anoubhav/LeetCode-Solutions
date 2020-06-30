#include <bits/stdc++.h>
typedef long long ll;
#define endl "\n";
#define IOS ios::sync_with_stdio(0); cin.tie(0); 
using namespace std;

int roman2int(string s){
    unordered_map<string, int> r2i;
    r2i["I"] = 1;
    r2i["V"] = 5;
    r2i["X"] = 10;
    r2i["L"] = 50;
    r2i["C"] = 100;
    r2i["D"] = 500;
    r2i["M"] = 1000;
    r2i["IV"] = 4;
    r2i["IX"] = 9;
    r2i["XL"] = 40;
    r2i["XC"] = 90;
    r2i["CD"] = 400;
    r2i["CM"] = 900;

    int ans = 0;
    int i = 0;
    string key;
    while (i<s.size()){
        key = s[i] + ((i+1 < s.size()) ? string(1, s[i+1]): "");
        if (r2i.find(key)!=r2i.end()){
            ans += r2i[key];
            i += 2;
        }
        else{
            key = s[i];
            ans += r2i[key];
            i += 1;
        }
        // cout<<key<<" "<<i<<" "<<ans<<" "<<(r2i.find(key)!=r2i.end())<<endl;
    }
    return ans;
}

int better(string s){
    if (s.empty()) return 0;
    
    unordered_map<char, int> table = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}
    };
    
    int num = 0;
    for (int i = 0; i < s.length() - 1; ++i) {
        if (table[s[i]] < table[s[i + 1]]) {
            num -= table[s[i]];
        } else {
            num += table[s[i]];
        }
    }
    num += table[s.back()];

    return num;
}
int main(){
    string s;
    cin>>s;
    cout<<roman2int(s);
}