#include<iostream>
using namespace std;

int main(void){
	int n;
	cin>>n;
	for(int i=0;i<2*n-1;i++){
		if(i<n){
			for(int j=0;j<i;j++)
				printf(" ");
			for(int j=0;j<2*(n-i)-1;j++)
				printf("*");
		}
		else{
			for(int j=0;j<2*(n-1)-i;j++)
				printf(" ");
			for(int j=0;j<2*(i-n+1)+1;j++)
				printf("*");
		}
		puts("");
	}
}
