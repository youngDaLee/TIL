#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector<string> text;//���κ� �ؽ�Ʈ ������ string ����
    string str;
    while(getline(cin,str) && !str.empty()){//����ڷκ��� str�Է¹ް�, �� str�� ������� ���� �� ����
        text.push_back(str);//���Ϳ� str����
    }
    for(int i=0;i<text.size();i++){//str�ϳ��� ���
        cout<<text[i]<<endl;
    }
}