#include<iostream>
#include<vector>
using namespace std;


//�̰� �� �¾�????
int main(){
    vector<string> text;//���κ� �ؽ�Ʈ ������ string ����
    string str;

    while(getline(cin,str)){//����ڷκ��� str�Է���
        text.push_back(str);//���Ϳ� str����
    }
    for(int i=0;i<text.size();i++){//str�ϳ��� ���
        cout<<text[i]<<endl;
    }
}