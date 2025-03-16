# EC2 기초
- ElastiComputeColud = IaaS(Infrastructure as a Service)
- 여러 기능을 포괄하는 기능
  - EC2 : Virtual Machine
  - EBS : 가상 드라이브
  - ELB : 여러 머신에 로드를 분산
  - ASG : 오토 스케일링 그룹

EC2 옵션
- OS : Linux, Window, MacOS
- CPU
- RAM
- Storage space
  - EBS & EFS
  - hardward(EC2 Instance Store)
- 네트워크 유형(Public IP, 네트워크 카드)
- Firewall rules
- Bootstrap script : EC2 User Data
  - bootstrapping : 머신이 시작할 때 실행시키는 스크립트. 시작할 때 한 번 실행됨. 부팅 작업을 자동화함
- EC2사용자는 루트로 실행

key pair format
- .pem : Window, Mac, Linux
- .ppk : Window 10 미만(7,8 등..)

