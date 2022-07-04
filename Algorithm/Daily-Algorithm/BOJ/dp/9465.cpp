#include<iostream>
using namespace std;

int main(void){
    int T;cin>>T;
    for(int testcase=0;testcase<T;testcase++){
        int n;cin>>n;
        int stk[2][n+1];
        int dp[2][n+1];

        for(int i=0;i<2;i++)
            for(int j=1;j<=n;j++)
                cin>>stk[i][j];

        dp[0][0]=0;dp[1][0]=0;
        dp[0][1]=stk[0][1];dp[1][1]=stk[1][1];
        for(int i=2;i<=n;i++){
            dp[0][i]=max(dp[1][i-1],max(dp[1][i-2],dp[0][i-2]))+stk[0][i];
            dp[1][i]=max(dp[0][i-1],max(dp[1][i-2],dp[0][i-2]))+stk[1][i];
        }
        int max_num=max(dp[0][n],dp[1][n]);
        cout<<max_num<<endl;
    }
}