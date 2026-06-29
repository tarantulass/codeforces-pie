//sounds similar to gas station problem in leetcode
/*
given that 0 and x dont have stations, there are n stations between these points
only there gas can be filled fully no fractions
aim - find min possible volume of gas in liters to travel from 0 to x and back to 0
*/


#include<bits/stdc++.h>
using namespace std;
//using ll=long long;
// as x is max 100

int main(){
	int t, n, x, a, minval;
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>n>>x;
		vector<int> v;
		for(int j=0;j<n;j++){
			cin>>a;
			v.push_back(a);
		}
		minval = v[0]; // as the start is 0
		for(int j=0;j<n-1;j++){
			minval = max(v[j+1]-v[j], minval);
		}
		minval = max(2*(x - v[n-1]), minval);
		cout<<minval<<endl;
	}

}
