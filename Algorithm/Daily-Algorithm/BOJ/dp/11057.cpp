#include<iostream>
using namespace std;

int main(void){
    int n;cin>>n;
    int dp[n+1][10];

    for(int i=0;i<10;i++)
        dp[1][i]=1;
    
    for(int i=2;i<=n;i++){
        dp[i][0]=dp[i-1][0];
        for(int j=1;j<10;j++)
            dp[i][j]=(dp[i][j-1]+dp[i-1][j])%10007;
    }

    int sum=0;
    for(int i=0;i<10;i++)
        sum=(sum+dp[n][i])%10007;
    cout<<sum<<endl;
}