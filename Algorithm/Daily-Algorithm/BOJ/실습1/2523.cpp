#include<iostream>
using namespace std;

int main(void){
	int n;
	cin>>n;
	for(int i=1;i<2*n;i++){
		if(i<=n){
			for(int j=0;j<i;j++)
				printf("*");
		}
		else{
			for(int j=0;j<2*n-i;j++)
				printf("*");
		}
		puts("");
	}
}
