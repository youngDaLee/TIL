#include<iostream>
#include<cmath>
using namespace std;

int main(void){
    int n;
    cin>>n;
    int dp[n+1];

    dp[1]=1;
    for(int i=2;i<=n;i++){
        dp[i]=dp[i-1]+1;
        if(0==sqrt(i)-(int)sqrt(i)){
            dp[i]=1;
            continue;
        }
        for(int j=1;j*j<i;j++){
            dp[i]=min(dp[i],dp[i-j*j]+1);
        }
    }
    cout<<dp[n]<<endl;
}