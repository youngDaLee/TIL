#include<iostream>
using namespace std;

int main(void){
	int n;
	cin>>n;
	
	for(int i=1;i<10;i++){
		printf("%d * %d = %d\n",n,i,n*i);
	}
	return 0;
}
