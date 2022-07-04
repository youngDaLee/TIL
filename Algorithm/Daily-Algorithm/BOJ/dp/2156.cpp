#include<iostream>
using namespace std;

int main(void){
    int n;cin>>n;
    int grape[n+1];
    for(int i=1;i<=n;i++)
        cin>>grape[i];
    
    long dp[n+1];
    dp[0]=0;dp[1]=grape[1];dp[2]=dp[1]+grape[2];
    for(int i=3;i<=n;i++)
        dp[i]=max(max(dp[i-2],dp[i-3]+grape[i-1])+grape[i],dp[i-1]);
    long max_num=max(dp[n],dp[n-1]);
    cout<<max_num<<endl;
}