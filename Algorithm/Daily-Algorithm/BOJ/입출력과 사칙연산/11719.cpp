#include<iostream>
#include<vector>
using namespace std;


//이게 왜 맞아????
int main(){
    vector<string> text;//라인별 텍스트 저장할 string 백터
    string str;

    while(getline(cin,str)){//사용자로부터 str입력음
        text.push_back(str);//백터에 str넣음
    }
    for(int i=0;i<text.size();i++){//str하나씩 출력
        cout<<text[i]<<endl;
    }
}