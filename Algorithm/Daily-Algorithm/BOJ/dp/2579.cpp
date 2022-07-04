#include<iostream>
using namespace std;

int main(void){
    int n;cin>>n;
    int arr[n+1];
    for(int i=1;i<n+1;i++)
        cin>>arr[i];
    
    int dp[n+1];
    dp[0]=0;dp[1]=arr[1];dp[2]=dp[1]+arr[2];
    for(int i=3;i<=n;i++){
        if(dp[i-2]<arr[i-1]+dp[i-3])//직전계단+i-3번째 계단이 i-2번째 계단까지 올라간수보다 크면
            dp[i]=arr[i]+arr[i-1]+dp[i-3];
        else
            dp[i]=arr[i]+dp[i-2];
    }
    cout<<dp[n]<<endl;
}