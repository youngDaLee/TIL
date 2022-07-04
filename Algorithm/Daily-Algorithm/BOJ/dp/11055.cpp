#include<iostream>
using namespace std;

int main(void){
    int n;cin>>n;
    int arr[n+1];
    int idx[n+1];
    for(int i=1;i<=n;i++)
        cin>>arr[i];
    
    int max_num=0;
    for(int i=1;i<=n;i++){
        idx[i]=1;
        for(int j=1;j<i;j++){
            if(arr[i]>arr[j])
                idx[i]=max(idx[i],idx[j]+1);
        }
        max_num=max(max_num,idx[i]);
    }
}