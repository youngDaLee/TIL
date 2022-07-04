#include<iostream>
#include<algorithm>//min들어있는 라이브러리
using namespace std;

int main(void){
    int n;
    cin>>n;
    int dp[n+1];//우리의 목표: dp[n]에 저장되어있는 수(연산 3개로 1을 만드는 것)
    //bottom-up 방식으로 i가 1부터 n까지 올라감
    int i=2; dp[1]=0;//i=1일때는 0번째로 1에 도달할 수 있음.
    while(i!=n+1){
        dp[i]=dp[i-1]+1;//규칙 3(1을 뺀다)
        if(i%2==0)
            dp[i]=min(dp[i],dp[i/2]+1);//규칙 2(2로 나누어 떨어지면 2로 나눈다)->규칙 3과 규칙2중 작은거 적용시킴.
        if(i%3==0)
            dp[i]=min(dp[i],dp[i/3]+1);//규칙 3(3으로 나누어 떨어지면 3으로 나눔)->규칙 3,2,1중 작은거 적용
        i++;
    }
    cout<<dp[n]<<endl;
}