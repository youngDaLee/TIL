#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector<string> text;//라인별 텍스트 저장할 string 백터
    string str;
    while(getline(cin,str) && !str.empty()){//사용자로부터 str입력받고, 그 str이 비어있지 않을 때 까지
        text.push_back(str);//백터에 str넣음
    }
    for(int i=0;i<text.size();i++){//str하나씩 출력
        cout<<text[i]<<endl;
    }
}