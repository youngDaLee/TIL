#include<iostream>
using namespace std;

int main(void){
    int n;cin>>n;
    int dp[n+1];
    dp[1]=1;dp[2]=2;
    for(int i=3;i<=n;i++)
        dp[i]=(dp[i-1]+dp[i-2])%10007;//왜 10007로 나누라고 할까?-괄호 안해서 계속 틀렸음 이런..
    cout<<dp[n]<<endl;
}