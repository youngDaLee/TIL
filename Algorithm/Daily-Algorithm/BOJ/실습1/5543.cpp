#include<iostream>
using namespace std;

int main(void){
	int price;
	int min_b=2000;
	int min_d=2000;
	for(int i=0;i<3;i++){
		cin>>price;
		if(price<min_b)
			min_b=price;
	}
	for(int i=0;i<2;i++){
		cin>>price;
		if(price<min_d)
			min_d=price;
	}
	int total=min_b+min_d-50;
	cout<<total<<endl;
} 
