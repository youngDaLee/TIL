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


