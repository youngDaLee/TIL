#include<iostream>
using namespace std;

int main(void){
	int n;
	cin>>n;
	for(int i=1;i<=2*n;i++){
		if(i%2==0){//Â¦¼ö 
			for(int j=1;j<=n;j++){
				if(j%2==0)
					printf("*");
				else
					printf(" ");
			}
		}
		else{//È¦¼ö 
			for(int j=1;j<=n;j++){
				if(j%2==0)
					printf(" ");
				else
					printf("*");
			}
		}
		puts("");
	}
}
