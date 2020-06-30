#include <bits/stdc++.h>
typedef long long ll;
#define endl "\n";
#define IOS ios::sync_with_stdio(0); cin.tie(0); 
using namespace std;

bool method1(int x){
    if (x < 0 || (x%10 == 0 && x!=0)) return false;
    int rev = 0;
    while (rev < x){
        rev = rev*10 + x%10;
        x /= 10;
    }
    //no. of digits is even || odd
    if (rev == x || rev/10 == x) return true;
    return false;
}

bool method2(int x){
    string s = to_string(x);
    string scopy = s;
    reverse(s.begin(), s.end());
    if (s == scopy) return true;
    return false;
}


int main(){
    int x;
    cin>>x;
    cout<<method1(x)<<endl;
    cout<<method2(x)<<endl;
}