# IAM 및 AWS CLI

IAM = Identity and Access Management, Global service
* 사용자를 생성하고, 그룹에 배치
* 글로벌 서비스에 해당(특정 리전에 종속되지 않음)
* Root account : 계정 생성할 때 기본으로 생성되는 것 -> 계정을 생성할 때만 사용해야 함. 루트 계정을 사용해서도 공유해서도 안됨.
* Users : 하나의 유저는 organization내의 한 user에 해당. user들을 group으로 묶을 수도 있음
* Groups : 유저를 묶을 수 있지만 다른 그룹을 포함시킬 수는 없음
  * 그룹에 묶이지 않는 유저도 존재할 수 있음 -> 추천하지는 않지만 가능
  * 하나의 사용자가 여러 그룹에 포함될 수 있음

IAM:Permission
* JSON 문서로 권한 부여
* 유저 또는 그룹별로 권한을 부여
* AWS에서는 최소 권한의 원칙을 적용 -> for 보안..
  * 유저가 꼭 필요로 하는 권한 이상의 권한을 부여하지 않는다

## IAM 실습
- IAM은 글로벌 서비스
- IAM Dashboard의 AWS Account에서 Account Alias를 설정하면, 해당 alias로 설정된 url에서 계정 로그인이 가능하다

IAM 정책 구조
- Version : `2012-10-17` 과 같이 policy language version
- Id : 정책 식별 id(optional)
- Statement : 구성 요소 (required)
  - Sid : statement 식별자 (optional)
  - Effect : statement가ㅣ 특정 api에 접근하는걸 허용할지/거부할지(Allow, Deny)
  - Principal : account/user/role
  - Action : effect에 기반해 allow or deny되는 api 호출 목록
  - Resource : 적용될 action의 리소스 목록
  - Condition : state가 언제 적용될지(optinal)


IAM에서 정책을 그룹에 넣어 추가 할 수도 있고, 유저에게 직접 추가 할 수도 있다

Policies에서 권한을 커스터마이징 할 수 있다
- 특정 버킷 리소스에 접근 허용을 하는 등으로 활용할 수 있을듯

## IAM MFA
유저와 그룹 보안 강화하는 방법
1. Password Policy (비밀번호 정책 정의)
   - AWS에서는 다양한 password policy 지정 가능(최소 비밀번호 길이, 대소문자숫자, 물음표 등)
   - IAM유저가 비밀번호 변경 부가하게 설정 가능
   - 90일마다 비밀번호 변경해야 하도록 설정 가능
   - 비밀번호 재사용 방지
   - 등등...
2.MFA (MultiFactor Authentication)
   - AWS에서 필수 권장 사항
   - MFA : password + security device you own

MFA devices options in AWS
- Virtual MFA device : 핸드폰에 설치 가능한 Google Authenticator, Auty등
- Universla 2nd Factor : 물리장치(usb형식의) YubiKey등...
- Hardware Key Fob MFA Device : 젬알토 등(번호를 수동으로 확인 가능)
- Hardware Key Fob MFA Device for AWS GovCloud(US) : 미국정부 클라우드 쓰고 있으면 SurePass 사용 가능...

## AWS Accesekey, CIL, SDK
AWS에 접근하는 방법
- 관리 콘솔(ManagementConsole) : pw+MFA
- CIL : access key로 보호됨
- SDK : code에서 접근

AccessKey 생성 방법
- IAM > Uesr > 유저별로 Create access key
- 내 콘솔에서 `aws config` 로 설정....

AWS 클라우드쉘
- 일부 리전에서만 사용 가능
- AWS에서 제공하는 쉘

## IAM Role
- AWS가 사용하는 롤...
- Common roles : EC2 인스턴스롤, Lambda Function Role, CloudFormation Role, ... 등

보안도구
- Credentials Report(account-level) : credential 상태를 리포트로 다운받아 볼 수 있음(csv)
- Access Advisor(user-level) : 유저에게 부여된 서비스 권한과 유저의 마지막 접속 시간 확인 가능

IAM 모범사례
- AWS 계정설정 할 때를 제외하고는 루트계정을 사용하지 말 것
- One physical user = One AWS user
- 유저를 그룹에 할당하고, 그룹에 권한을 할당해서 보안이 그룹 수준에서 관리되도록 해야 함
- 강력한 password policy를 만들 것 
- MFA를 사용하여 보안 강화할 것
- Roles를 생성하여 권한을 부여할 것
- IAM Credentials Report, Access Advisor로 관리하고
- IAM user, Access Key를 절대 공유하지 말 것

## IAM의 공동 책임 모델 (Shard Responsibility Model)
- AWS가 책입지는것 : Infrastructure, Configuraation, vulneability analysis, Compliance validation
- 나 : User/MFA/IAM tools/permision 등

## Quiz

1) IAM 역할의 올바른 설명은?
- AWS 서비스에서 사용할 AWS 서비스 요청을 위한 권한 집합을 정의하는 IAM 엔터티

2) IAM 보안도구는?
- IAM 자격증명 모고서

3) IAM 유저와 관련하여 잘못된 것은?
- IAM 사용자는 루트 계정 자격증명을 사용하여 AWS 서비스에 액세스 합니다

4) IAM 모범사례는?
- 루트 계정을 사용하지 않음

5) IAM 정책(policy)는?
- AWS서비스에 요청을 보내는 권한의 집합을 정의하고 IAM 사용자, 사용자 그룹 및 IAM 역할이 사용할 수 있는 JSON 문서

6) IAM 권한 에서 어떤 원칙을 지켜야 하는지
- 최소 권한 부여

7) 루트 계정 보안을 높이려면?
- MFA 활성화

8) IAM 유저그룹에는 IAM 유저 및 기타 사용자 그룹이 포함될 수 있다
- 거짓 : 유저만 포함 가능(그룹 포함 불가)

