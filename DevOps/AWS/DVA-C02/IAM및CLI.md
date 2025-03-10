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
