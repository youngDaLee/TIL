#include<iostream>
using namespace std;

int main(void){
    int testcase;
    cin>>testcase;
    for(int i=0;i<testcase;i++){
        int a,b;
        scanf("%d,%d",&a,&b);//scanf���� ""�ȿ� ,�� ���� ���� �װ� �����ϰ� �Է¹���.
        printf("%d\n",a+b);
    }
}