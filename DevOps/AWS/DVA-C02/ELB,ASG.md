# ELB(Elastic Load Balancing)
## 로드밸런싱이란
- 트래픽을 여러 인스턴스(EC2등)에 분산시키는 것

헬스체크
- ELB의 EC2가 적당히 동작하고 있는지 확인하는 것
- port와 route에서 동작
  - 4567 port, /health endpoint
- 200(OK) 상태의 EC2에만 트래픽을 보냄