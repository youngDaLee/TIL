#include<iostream>
using namespace std;

int main(void){
	ios_base :: sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
/*��ó: https://eine.tistory.com/entry/CC-�����-�����-����-�ӵ�-���� [���ν�Ʈ���� SW ��α�]*/

	int T;
	cin>>T;
	
	int a,b;
	for(int i=0;i<T;i++){
		cin>>a>>b;
		printf("%d\n",a+b);
	}
	return 0;
}
