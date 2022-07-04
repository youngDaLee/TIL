#include<iostream>
using namespace std;

int main(void){
    int n;cin>>n;
    int dp[n+1][10];

    for(int i=0;i<10;i++)//n=1인 경우
        dp[1][i]=1;
    
    for(int i=2;i<=n;i++){
        dp[i][0]=dp[i-1][1];
        dp[i][9]=dp[i-1][8];
        for(int j=1;j<9;j++)
            dp[i][j]=(dp[i-1][j-1]+dp[i-1][j+1])%1000000000;
    }
    
    int sum=0;
    for(int i=1;i<10;i++)
        sum=(sum+dp[n][i])%1000000000;
    cout<<sum<<endl;

}