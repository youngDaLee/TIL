#include<iostream>
using namespace std;

int main(void){
	int n,x;
	cin>>n>>x;
	int a[n];
	int num;
	for(int i=0;i<n;i++){
		cin>>num;
		a[i]=num;
	}
	for(int i=0;i<n;i++){
		if(a[i]<x)
			printf("%d ",a[i]);
	}
	puts("");
	
	return 0;
}
