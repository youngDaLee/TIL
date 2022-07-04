#include<iostream>
using namespace std;

int main(void){
	int T;
	cin>>T;
	
	int a,b;
	for(int i=0;i<T;i++){
		cin>>a>>b;
		printf("Case #%d: %d\n",i+1,a+b);
	}
	return 0;
}
