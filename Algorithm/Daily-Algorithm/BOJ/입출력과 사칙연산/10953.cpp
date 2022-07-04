#include<iostream>
using namespace std;

int main(void){
    int testcase;
    cin>>testcase;
    for(int i=0;i<testcase;i++){
        int a,b;
        scanf("%d,%d",&a,&b);//scanf에서 ""안에 ,등 무언가 들어가면 그거 제외하고 입력받음.
        printf("%d\n",a+b);
    }
}