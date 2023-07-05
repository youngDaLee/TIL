### 0. github 계정등록
`git config --global user.emal "깃허브 메일 계정"`     
`git config --global user.name "깃허브 이름"`        
으로 깃허브 초기 세팅(계정 등록 및 비번 등록)

### 1.git init
github 원격과 연동할 **빈 폴더**를 생성       
![git01](/.img/basic01.png)
cmd창(혹은 git cmd창)을 켜고, 해당 폴더로 이동해준 뒤      
`git init` 을 해 준다.
![git01](/.img/basic02.png)          
폴더에 .git 파일이 보이면 git init 성공

### 2.git remote add origin
![git01](/.img/basic03.png)     

원격저장소 주소 복사해 온 뒤
![git01](/.img/basic04.png)        
`git remote add origin <원격저장소 주소>`         
명령어를 입력      

![git01](/.img/basic05.png)      

원격 저장소와 연결완료

### 3.git remote update
원격 저장소와 연동이 되었으면, 원격 저장소에서 브랜치들을 불러옴
![git01](/.img/basic06.png)
      
`git remote update` 명령으로 원격 브랜치들을 불러옴.              
위 화면과 같이 원격 저장소에 있는 모든 브랜치들이 출력되었다면 완벽하게 완료.
        
이제 cmd창 종료 후 VSCode로 작업.
 
### 4.VScode 브랜치 선택 및 바로 pull
해당 폴더에서 바로 우클릭해서 vscode를 열기      
![git01](/.img/basic07.png)         
vscode 열었으면, 좌측 하단에 깃허브 모양 아이콘 클릭
![git01](/.img/basic08.png)     
이렇게 방금 `git remote update` 로 불러왔던 원격브랜치들이 불러져 있음
![git01](/.img/basic09.png)      
여기서 원하는 브랜치를 클릭해주면 해당 브랜치의 HEAD로 폴더가 변경됨
- **주의사항** : 브랜치 선택하자마자 강제 pull 됨. vscode에서 브랜치 변경할때는 가능한 해당 폴더에 아무것도 없는 빈폴더이게 해야함. 아니면 걍 다 날라감.

![git01](/.img/basic10.png)
vscode 폴더 목록 보면 원격의 develop 브랜치랑 똑같은 모양으로 업데이트됨

### 5. VSCode에서 add - commit -push
![git01](/.img/basic11.png)    
파일이 변경되었으면 깃허브 아이콘 옆에 숫자가 떠 있음    

![git01](/.img/basic12.png)       
Changes 에는 변경된 파일들(커밋을 기다리는 파일들)이 들어가 있음. 해당 이미지에서는 총 7개 파일이 변경됨
 
![git01](/.img/basic13.png)        
이 파일들을 한번에 add할수도 있고, 한개씩 add할수도 있음.      
맨 오른쪽 + 를 클릭하면 스테이지에 올라감.      
커밋 메세지 단위대로 끊어서 add(+)해서 스테이지에 올려주고 커밋하고,
또 새로운 단위의 작업을 스테이지에 add(+)해서 커밋하면 됨.

저 파일들이 하나의 작업이라 한번에 올리도록 하겠습니다.
![git01](/.img/basic14.png)    
Changes에는 파일이 없고(내가 한번에 다 올렸으니까)     
Staged Changes에 모든 파일들이 올라가 있는 걸 확인할 수 있음.      
Staged Changes 바로 위에 Message (Ctrl+Enter to ... ) 에 커밋 메세지 쓰면 됨.      

![git01](/.img/basic15.png)    
이렇게 커밋 메세지까지 작성이 완료되었으면, 맨 위에 Source Control 옆에 체크표시를 눌러 커밋.       

![git01](/.img/basic16.png)    
커밋이 완료되면 아무것도 없던 것처럼 비게 됨
 
![git01](/.img/basic17.png)    
Source Control 탭의 쩜쩜쩜을 눌러주면 깃의 기능들이 나옴.     
Push를 클릭해 Push해줌       
 
![git01](/.img/basic18.png)    
푸시 성공