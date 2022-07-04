#include<iostream>
using namespace std;

int main(void){
	int n;
	cin>>n;
	int nnum=n;
	int cnt=0;
	do{
		int num=(n%10)+(n/10);
		if(num>9){
			num-=10;
		}
		n=(n%10)*10+num;
		cnt++;
	}while(n!=nnum);
	printf("%d\n",cnt);
} 
