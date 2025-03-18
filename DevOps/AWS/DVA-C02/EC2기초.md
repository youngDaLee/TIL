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

## EC2 인스턴스 타입
> https://aws.amazon.com/ko/ec2/instance-types/

네이밍 컨벤션
- m5.2xlarge
  - m : 인스턴스 클래스
  - 5 : 인스턴스 세대(generation) (AWS improves them over time)
  - 2xrage : 인스턴스 클래스 내 크기. 크기가 클 수록 더 많은 메모리, CPU를 가짐

General(범용)
- 웹 서버, 코드 저장소 같은 자양한 작업에 적합
- Compute, Memory, Networking 밸런스도 잘 맞음

Compute Optimize(컴퓨팅 최적화)
- 컴퓨팅 집약접 작업(compute-intensive)에 적합
  - batch, media, 고성능 웹서버, 고성능 컴퓨팅(HPC, High performance computing), 머신러닝, 게이밍 서버
- c로 시작하는 이름을 가짐(c5, c6, ...)

Memory Optimized(메모리 최적화)
- 메모리(RAM)에서 대규모 데이터셋 처리하는 유형 작업에 최적화
  - 고성능 RDB/in-memory DB, web scale cache store, BI, 대규모 비정형 데이터 실시간 처리를 하는 애플리케이션
- R, X, ... 

Storage Optimize(스토리지 최적화)
- 대규모 데이터셋에 액세스할 때 적합
  - OLTP, RDB, NoSQL, Redis같은 캐시(in-memory db), Data warehouse, 분산 파일 시스템
- I, G, H1, ..

## Security Groups
- IP를 기준으로 보안그룹을 설정 가능
- 보안그룹 끼리 서로 참조 가능
- 인스턴스:보안그룹은 n:n
  - 하나의 보안그룹으로 여러 인스턴스 그룹에 적용 할 수 있음
  - 인스턴스 그룹에 여러 보안그룹 적용 가능
- revion/VPC에 적용됨. 지역별로 새로 보안그룹 생성해야함
- EC2 외부에 존재. EC2 외부의 인스턴스 방화벽
- SSH 액세스를 위해서는 별도의 보안그룹을 생성하는 것이 좋음
- 애플리케이션에 접근할 수 없는 것은 보안그룹 이슈임(타임아웃)
- connection refused가 나면 보안그룹 외의 다른 문제임. 보안그룹 작동해서 트래픽 통과했는데 애플리케이션단에서 거부난 것
- default
  - inbound traffic은 모두 block
  - outbound traffic은 모두 allow


classic ports
- 22 = SSH(SecureShell) : 리눅스에서 EC2인스턴스에 로그인 가능
- 21 = FTP(File Transfer Protocol) : 파일 업로드
- 22 = SFTP(Secure File Transfer Protocol) : SSH를 이용해 파일 업로드
- 80 = HTTP
- 443 = HTTPS
- 3389 = RDP(Remote Desktop Protocol) : 윈도우에서 로그인하기 위함


## SSH
- mac, linux, windows 10 이상에서 사용 가능
- windows 10 미만에서는 putty 사용(window 10이상에서도 putty 사용 가능)
- EC2 Instance Connect를 통해서는 mac, linux, windows 10 이하, 이상 모두 사용 가능
