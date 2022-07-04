#include<iostream>
using namespace std;

int main(void){
    int n;cin>>n;
    int p[n+1];//카드팩
    int dp[n+1];
    for(int i=1;i<=n;i++)
        cin>>p[i];
    
    dp[1]=p[1];
    for(int i=2;i<=n;i++){
        dp[i]=p[i];

        for(int j=1;j<i;j++){
            dp[i]=max(dp[i],dp[i-j]+p[j]);
        }
    }
    cout<<dp[n]<<endl;
}