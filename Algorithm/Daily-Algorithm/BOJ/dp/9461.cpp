#include<iostream>
#include<algorithm>
using namespace std;

int main(void){
    int T;
    cin>>T;
    
    long long dp[101]={0,1,1,1,2,2, };
    for(int i=6;i<101;i++){
        dp[i]=dp[i-1]+dp[i-5];
    }

    for(int i=0;i<T;i++){
        int n;
        cin>>n;
        cout<<dp[n]<<endl;
    }

}