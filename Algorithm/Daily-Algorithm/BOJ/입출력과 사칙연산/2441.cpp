#include<iostream>
using namespace std;
int main(){
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        for(int j=0;j<i;j++)
            cout<<" ";
        for(int j=t;j>i;j--)
            cout<<"*";
        printf("\n");
    }
} // namespace std;
