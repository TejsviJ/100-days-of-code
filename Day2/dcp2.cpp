#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

	

int func(int x, vector<int>& v,vector<int>& b){
	int p=1;
	for(int i=0;i< v.size();i++){	
	if(i!=x){
		p=p*v[i];
	}
}
	x+=1;
	b.push_back(p);
	if(x<v.size()){
		func(x,v,b);
	}		
for (int z = 0;z<v.size();z++) {
		
		return b[z];
	}
}
int main(){
	int x=0;
		vector<int> v,b;
		int a;
	for (int i=0;i<5;i++){       //generating a simple vector 
		cin>>a;
		v.push_back(a);
	}
		 func(x,v,b);
	for (int z = 0;z<v.size();z++) {
		cout<< b[z]<<endl;
	}
}
