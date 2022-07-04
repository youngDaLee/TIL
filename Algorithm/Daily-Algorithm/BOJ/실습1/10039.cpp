#include<iostream>
using namespace std;

int main(void){
	int a,b,c,d,e;
	cin>>a>>b>>c>>d>>e;
	if(a<40)
		a=40;
	if(b<40)
		b=40;
	if(c<40)
		c=40;
	if(d<40)
		d=40;
	if(e<40)
		e=40;
	double avg=(double)(a+b+c+d+e)/5;
	cout<<avg<<endl;
}
