#include<iostream>
using namespace std;

int main(void){
	int a,b,c;
	cin>>a>>b>>c;
	int sec;
	if((a>=b && a<=c) || (a>=c && a<=b))
		sec=a;
	else if((b>=a && b<=c) || (b>=c && b<=a))
		sec=b;
	else
		sec=c;
	cout<<sec<<endl;
}
