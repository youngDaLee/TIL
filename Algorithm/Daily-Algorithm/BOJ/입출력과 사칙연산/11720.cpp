#include<iostream>
using namespace std;

int main(){
    int T;
    string str;
    cin>>T>>str;

    int sum=0;
    for(int i=0;i<T;i++){
        int num=(int)str[i]-48;//ASCII num¿¡ ¸Â°Ô 48 »©ÁÜ
        sum+=num;
    }
    cout<<sum<<endl;
}