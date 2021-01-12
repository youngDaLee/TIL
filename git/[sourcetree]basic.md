# SourceTree로 Github 사용하기
- sourcetree로 github에 소스 업로드하고 공유하기
- 업로드할 파일 선택하고 add -> commit -> push
## 절차
1. github 가입
2. github repository 생성
3. github repository 클론
4. 내 컴퓨터 내 문서 아래에 생성된 프로젝트 디렉토리에서 파일 생성 및 작업 완료
5. 커밋할 파일들 선택해서 스테이지 올리기(add)
6. 커밋하기(commit)
7. 푸시하기(push)

## git 이란?
형상 관리 시스템(Verson Control System)의 한 종류. 주로 개발다들이 프로그램과 관련되 파일 저장하는데 사용. 게임의 세이브 포인트와 같이 언제든 저장 시점으로 되돌아 갈 수 있음. 이 외에도 CVS, SVN등이 있다.
### git vs github
Git은 Git repository라 불리는 데이터 저장소에 소스 코드 등을 넣어 이용하는 것.     
GitHub는 이러한 Git repo를 인터넷 상에서 제공하는 서비스(호스팅 서비스). GitHub에서 공개되는 소스 코드들을 Git으로 관리.

## 용어 정리
|용어|설명|
|----|-------------|
|Repository, Repo (origin)|프로젝트 파일들 저장하는 공간(원격저장소)|
|Branch(브랜치)|독립적인 작업 공간. Repo최초 생성 시 'master'브랜치 생성|
|HEAD|현재 작업중인 브랜치|
|checkout|브랜치 선택하는 작업|
|fork|다른 사람의 Repo를 나의 Repo로 복사하는 작업|
|clone|Repo를 로컬 저장소(내 컴퓨터)로 다운받는것|
|master|Repo 최초 생성 시 존재하는 main branch|
|.git|폴더 안의 작업물들 버전 관리하는 폴더. .git이 있는 폴더는 로컬 저장소가 된다|
|upstream|내가 Fork한 다른 사람의 저장소|
|add|커밋하기 전 버전관리를 원하는 파일들 묶는 일. 스테이지에 파일을 올리는 것|
|commit|버전관리 할 파일 및 폴더에 설명을 다는 것.|
|remote|github의 저장소와 연결할 때 쓴다|
|fetch|remote repository의 특정 브랜치 내용 가져오는 것|
|pull(=fetch + merge)|remote repo.의 특정 브랜치의 내용 가져와 현재 HEAD가 가리키는 브랜치에 merge하는 것|
|pull request|내 repo에서 작업한 것들을 fork 뜬 곳으로 반영시켜 달라 요청하는 것|
|merge|현재 브랜치가 가리키는 커밋과 다른 브랜치가 가리키는 커밋 합치는 것|
|rebase|현재 브랜치가 가리키는 커밋을 다른 브랜치가 가리키는 커밋 뒤에 그대로 잇는 것|

    
### 커밋 메세지
[좋은 git commit 메세지를 위한 영어 사전](https://blog.ull.im/engineering/2019/03/10/logs-on-git.html)
- Feat : 새로운 기능 추가
- Fix : 버그 수정
- Docs : 문서 수정
- Style : 포맷 수정(코드 수정x)
- Refactor : 규격 수정(탭 정리 등.. 코드 수정X)
- Test : 테스팅

### Gitflow Branch
- Master branch : 제품으로 출시 될 수 있는 브랜치(배포(Release)가능한 상태만을 관리)
- Develop branch : 다음 출시 버전 개발(모든 기능 추가됨+배포가능)
- Feature branch : 기능 개발(각 로컬에서 새로운 기능 개발 및 버그 수정, 개발 완료되면 develop에 병합)
- Release branch : 이번 출시 버전 준비
- Hotfix branch : 출시 버전에서 발생한 버그 수정

## .gitignore
Git에서 관리하면 안되는 파일/폴더 혹은 올리고 싶지 않은 파일/폴더를 미리 지정하여 관리 대상에서 제외시키기 위해 있는 파일.     
[gitignore 파일 설정 및 반영](https://blog.naver.com/PostView.nhn?blogId=simpolor&logNo=221065977618&categoryNo=27&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=&from=postList&userTopListOpen=true&userTopListCount=5&userTopListManageOpen=false&userTopListCurrentPage=1)