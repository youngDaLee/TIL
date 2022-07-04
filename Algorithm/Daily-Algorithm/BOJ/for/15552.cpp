#include<iostream>
using namespace std;

int main(void){
	ios_base :: sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
/*출처: https://eine.tistory.com/entry/CC-입출력-방법에-따른-속도-정리 [아인스트라세의 SW 블로그]*/

	int T;
	cin>>T;
	
	int a,b;
	for(int i=0;i<T;i++){
		cin>>a>>b;
		printf("%d\n",a+b);
	}
	return 0;
}
