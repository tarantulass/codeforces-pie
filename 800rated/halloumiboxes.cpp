// based on sorting !!
// sort in non decreeasing order
// machine sonly reverses atmost k len subarrays in the array
#include<bits/stdc++.h>
using namespace std;
using ll=long long;

// find whether we can sort with any number of reverses!!

/*
surely has somethign to do with the number of peak elements
as otherwise we have a nsqaured alsgo which will surely fail!
answer = no idiot think about sorting need for sorting when is it needed 
wehn does it guarantee the thign asked
*/

int main(){
	// initialize
	int t,n,k,a;
	cin>>t;
	for(int i=0;i<t;i++){
		vector<int> v;
		cin>>n>>k;
		for(int j=0;j<n;j++){
			cin>>a;
			v.push_back(a);
		}
		// in c++ it is inplace !!
		// k>=2 min conditon for sorting if we have to reverse etc..
		// less only if it i salready sorted!!
		vector<int> sortedv = v;
		sort(sortedv.begin(), sortedv.end());
		bool issorted = (sortedv==v);
		if(k>=2 or issorted){
			// simple bubble sort
			cout<<"YES"<<endl;
		}
		else{
			cout<<"NO"<<endl;
		}
	}
}
