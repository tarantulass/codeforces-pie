/*
question
1. 10x10 target made out of 5 rings as shown
2. outer most ring as always away from center has 1 points and closer to center has 5
*/

/*
attempts
simple tracking as we have 
*/

#include<bits/stdc++.h>
using namespace std;

int main(){
	int t, points;
	string row;
	for(int i=0;i<t;i++){
		points = 0;
		vector<string> board;
		for(int i=0;i<10;i++){
			cin>>row;
			board.push_back(row);
		}
		cout<<points<<endl;
	}
}
