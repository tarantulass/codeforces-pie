// always pass by reference to speed up
#include<bits/stdc++.h>

using std::strign;
using std::cin;
using std::cout;
using std::set;

void erasesubroutine(string s, set<string>& unique_s){
	if(s.size()<1){
		return;
	}
	unique_s.insert(s);

	// first is erase the first and then second is erase 2nd
	erasesubroutine(s(s.begin()+1,s.end()), unique_s);
	erasesubroutine(s[0] + s(s.begin()+2,s.end()), unique_s);

}

int main(){
	int testcases, slen;
	string s;

	cin>>testcases;
	for(int i=0;i<testcases;i++){
		cin>>slen;
		cin>>s;
		// also clear the set after every run otherwise ded
		set<string> unique_s;
		erasesubroutine(s);
		cout<<unique_s.size()-1<<endl;
// since we only want to count after the operations not the first one
	}
}
