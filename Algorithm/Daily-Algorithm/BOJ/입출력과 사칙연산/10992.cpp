#include<iostream>
using namespace std;

int main(void){
	int n;
	cin>>n;
	for(int i=1;i<=n;i++){
		if(i==n){
			for(int j=0;j<2*n-1;j++)
				cout<<"*";
			break;
		}
		for(int j=1;j<n+i;j++){
			if(j==n+i-1 || j==n-i+1){
				cout<<"*";
				continue;
			}
			cout<<" ";
		}
		puts("");
	}
}
