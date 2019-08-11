/*This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
*/
#include <iostream>
#include <stdio.h>
using namespace std;
int func(int* a,int K){
	for (int i=0;i<sizeof(*a);i=i+1){
		for (int j=i;j<sizeof(*a);j= j+1){
			if ((a[i]+a[j])==K){
				cout <<a[i]<<" and "<<a[j]<<endl;
			}
		}
	}
}

int main(){
	int b=17,a[4]={15,10,2,7};
	func(a,b);
	
return 0;
}
