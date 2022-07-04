#include<iostream>
using namespace std;

int main(void){
	int n;
	cin>>n;
	for(int i=1;i<=2*n-1;i++){
		if(i>n){
			for(int j=0;j<(n-(2*n-i));j++)
				cout<<" ";
			for(int j=0;j<(2*n-i);j++)
				cout<<"*";
			puts("");
			continue;
		}
		for(int j=0;j<n-i;j++)
			cout<<" ";
		for(int j=0;j<i;j++)
			cout<<"*";
		puts("");
	}
}
