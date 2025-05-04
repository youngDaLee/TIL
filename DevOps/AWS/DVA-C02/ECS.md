# ECS, ECR 및 Fargate
AWS에서 Docker Containers를 관리하는 방법
- ECS(Elastic Container Service) : 도커 관리를 위한 플랫폼
- EKS(Elastic Kubernetes Service) : 쿠버네티스 관리를 위한 플랫폼(오픈소스)
- Fargate : 서버리스 컨테이너 플랫폼
  - ECS, EKS 둘 다 함께 동작 가능
- ECS : 컨테이너 이미지 저장하는데 사용됨

## ECS
EC2 Launch Type
- AWS에서 도커 문서를 실행하면 ECS클러스터에서 ECS 태스크를 실행하는 것
- ECS 클러스터 구성요소
  - EC2 인스턴스(EC2 시작유형 사용할 때.. 인프라를 직접 프로비저닝하고 관리해야 함)
  - ECS클러스터 내부의 EC2인스턴스는 각 인스턴스가 ECS에이전트를 실행해야 하고, 이 에이전트가 ECS서비스와 지정된 ECS클러스터에 ECS인스턴스를 등록함


Fargate Launch Type
- 인프라를 프로비저닝 하지 않음(EC2 없음)
- 완전한 서버리스 방식
- ECS태스크만 정의하고나면 AWS에서 CPU, RAM요구사항만으로 서버를 띄워줌
- 새로운 도커 컨테이너를 실행할 때 EC2인스턴스 생성 없이 간단히 실행할 수 있다
- 확장하려면 태스크 수만 늘리면 됨.


IAM Role for ECS
- EC2 Instance Profile(EC2 LanchType일 때)
- ECS Task Role(EC2, Fargate)
  - 각역할을 다른 AWS서비스에 연결 가능


LoadBalance Integrations
- 모든 ECS Tasks를 LB로 관리할 때
- ALB지원.. -> 대부분의 활용사례가 지원됨
- Network LoadBalacer : 높은 스루풋, 성능이 요구되는 사례에, AWS Private Link를 사용하는경우 유용
- Elastic load Balancer : Fargate를 지원하지는 않고.. 고급기능 지원안해서 추천하지 않음


EFS(Data Volumes)
- EC2, Fargate 모두 호환됨
- 어느 AZ에서 실행중인 데이터에 활용됨..
- Fargate와 함께 사용하면 완전한 서버리스 방식으로 활용 가능. 사용량을 기반으로 요금이 청구됨
- 영구 다중 AZ방식
- S3를 ECS 태스크에 포함시킬수는 없음

