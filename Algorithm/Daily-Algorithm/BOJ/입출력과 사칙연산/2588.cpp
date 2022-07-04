#include<iostream>
using namespace std;

int main(void){
	int num1,num2;
	cin>>num1>>num2;
	
	int n1,n2,n3;
	int num_2=num2;
	n1=num2%10;
	num2=num2/10;
	n2=num2%10;
	num2=num2/10;
	n3=num2%10;
	
	cout<<num1*n1<<endl;
	cout<<num1*n2<<endl;
	cout<<num1*n3<<endl;
	cout<<num1*num_2<<endl;
}
