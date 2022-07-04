#include<iostream>
using namespace std;

int main(void){
    int n;cin>>n;
    long dp[n+1][2];
    dp[1][0]=1;dp[1][1]=1;
    for(int i=2;i<=n;i++){
        dp[i][0]=dp[i-1][0]+dp[i-1][1];
        dp[i][1]=dp[i-1][0];
    }
    cout<<dp[n][1]<<endl;
}