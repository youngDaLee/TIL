# 장고 기초
## 1. 기초
### 1-1. 웹 프레임워크와 Django
#### 프레임워크란?
- 자주 사용되는 코드를 체계화해서 쉽게 사용할 수 있도록 하는 코드 집합.
- 웹 개발에 필요한 기본적인 구조와 코드(함수, 클래스 등)가 만들어져 있음
- 라이브러리와의 차이점은
  - 규모 : 프레임워크>>>라이브러리
  - **프로젝트의 기반**이 됨
  - 건축에서 골조는 프레임워크, 그 외 자제가 라이브러리
  - 프레임워크는 **의존도**가 많이 높음. 제공해주는게 아주 많음.

#### 웹 프레임워크로서의 장고
[장고 공식 문서](https://docs.djangoproject.com/en/3.1/)   
앞으로 공식 문서 자주 봐야 함.
#### 모델, 뷰, 템플릿 계층
**모델**
- 데이터베이스와 연동하는 부분
- SQL이라는 별도의 문법 사용해야 함.
  - 장고에서는 파이썬 안에 있는 클래스로 만들고 **연결만 하면 sql 자동으로 처리**해줌.
- 여러 필드를 제공하고 필드의 옵션 입력할 수 있게 함
  - 데이터베이스가 아닌 프레임워크에서 해결!
- 모델 계층에서 제공하는게 한정적. sql 복잡. 얘를 프레임워크로만 처리하기에 한계가 있음
  - 좀 더 심화해서 사용하고 싶으면 아래 계층으로 가서 직접 sql 작성할 수 있게 함.

**뷰**
- 비즈니스 로직
- 비즈니스 로직에 필요한 부수적인거 다 제공
  - URL파싱, 요청, 응답
- 함수에서 정보를 담아 원하는 걸 파이썬 코드로 호출하고 반환

**템플릿**
- 디자이너에게 친숙한 문법 제공(html코드).
- html코드 안에서 사용가능한 문법들이 템플릿 계층
- html코드에서 반복문, 변수 사용하고 싶을 때 별도의 언어 제공
- 여러 문법 제공     

이 세 가지(MTV)가 핵심.   
**데이터를 정의하고(모델), 데이터를 가지고 어떤 동작을 하고(뷰), 동작된 결과로 뭘 보여주고(템플릿)**

### 1-2. 환경설정
#### 가상환경 설정
1. `virtualenv 가상환경이름` 으로 가상환경 생성
2. `가상환경이름/Scripts/activate` 혹은 `가상환경이름/bin/activate`로 가상환경 활성화

#### 장고 프로젝트 생성
1. `pip3 install django` 로 장고 설치
2. `django-admin startproject 프로젝트명` 으로 프로젝트 생성
3. `cd 프로젝트명` 으로 프로젝트로 이동한 뒤
4. `django-admin startapp 앱이름` 으로 앱 생성    

프로젝트?앱?
- 하나의 프로그램이 프로젝트
- 그 안에 여러 앱이 생성됨. 뷰,모델,템플릿(MTV)등의 하나의 묶음이 앱
- 앱이라는 단위로 분리해서 프로젝트 관리    


#### 앱 등록하기
프로젝트명/프로젝트명 폴더에 settings.py에서 여러 설정 관리
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
이렇게 settings.py의 INSTALLED_APPS에 앱 이름 추가하면 앱 등록됨
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'board',
    'fcuser'
]
```
이런식으로... 여기선 board와 fcuser 앱 등록함.

## 2. MTV
### 2-1. 마이그레이션
[마이그레이션 정리된 블로그(초보몽키님)](https://wayhome25.github.io/django/2017/03/20/django-ep6-migrations/)    
1. 마이그레이션 파일 생성
   - `python manage.py makemigrations`
   - migrations 폴더 안에 initial 파일 생성됨. 이 필드가 이러이러한게 있구나. 그럼 이렇게 DB를 만들어야겠다.
   - 이 명령을 통해 **자동으로 DB 생성**됨
2. 마이그레이션 적용
   - `python manage.py migrate`
   - settings의 앱들이사용하는 테이블 자동 생성해줌
   - db.sqlite3 파일 생성됨
     - 이 파일은 이미 settings에 설정되어 있음
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
} 
```
 - 이렇게! sqlite엔진을 사용하고 그 db파일은 ~~위치에 있다고 설명해주는 코드임
3. 마이그레이션 적용 현황
   - `python manage.py showmigrations`
4. 지정 마이그레이션의 SQL 내역
   - `python manage.py sqlmigrate`     

1, 2번 명령 계속 **반복**을 통해 클래스에 반영하는 수정사항들이 지속적으로 DB에 반영됨.

### 2-2. Admin


## 3. Static

## 4. 로그인

## 5. 게시판

## 6. 태그

## 7. 배포(Python anywhere)