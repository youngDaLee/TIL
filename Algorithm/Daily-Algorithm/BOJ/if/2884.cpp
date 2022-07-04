#include<iostream>
using namespace std;

int main(void){
	int h,m;
	cin>>h>>m;
	
	m-=45;
	if(m<0){
		m+=60;
		h--;
	}
	if(h<0)
		h=23;
	cout<<h<<" "<<m;
}
