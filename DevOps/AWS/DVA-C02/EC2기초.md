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

## EC2 구매 옵션
- On-Demand Instance : 요청에 따라 인스턴스를 실행가능. 단기 워크로드에 적합(가격 예측 가능, 초당 비용 지불)
- Reserved(1&3 years) (RI)
  - 긴 워크로드(DB등)
  - Convertible Reserved Instances
- Savings Plans (1& 3 years) : 특정 사용량을 약정하여 비용 지불
- Spot Instances : 아주 짧은 단기 워크로드용 인스턴스. 아주 저렵. 다만 언제든 인스턴스를 손실할 수 있어 신뢰성이 낮음
- Dedicated Hosts : 물리 서버를 분리시켜 놓는 것
- Deadicated Instance : 하드웨어를 공유하지 않음

RI
- 온디맨드에 비해 72%의 가격으로 사용 가능
- Instance Type, Region, Tenancy, OS등을 예약하여 사용
- 1년 or 3년을 선택 가능(3년 선택 시 할인률 올라감)
- 전체 선결제, 부분 선결제, 선결제 없는 옵션 모두 가능(전체 선결제시 할인률 올라감)
- 특정리전, AZ용량을 결정하여 범위 지정 가능
- DB등에 적합....
- 마켓플레이스에서 구매/되팔기 가능
- 종류
  - 전환형 인스턴스 : instance type, instance family, os, scope, tenancy 변경 가능 -> 대신 66% 할인...

Saving Plans
- RI와 비슷한 할인률(72%)
- RI보다 좀 더 유연성이 있음
- Flexible across
  - 인스턴스 사이즈(m5.xlarge, m5.2xlarge, ... )
  - OS
  - Tenancy (Host, Dedicated, Default)

Spot
- 90%까지 할인됨
- 인스턴스가 언제든 중단될 수 있음
- 스팟 인스턴스에 지불하고자 하는 가격보다 스팟 가격이 높으면 중단됨
- 가장 비용 효율적인 인스턴스
- 서비스가 중단되어도 복구가 쉬운 워크로드에 적합
  - 배치, 데이터분석, 이미지처리, 분산된 워크로드, 시작/종로 지점이 자유로운 워크로드 등...

Dedicated Hosts
- 물리 서버
- 규정 준수 요구사항이 있거나, 기존 서버 결합 소프트웨어 사용해야 할 시...
- 구매 옵션
  - On-demand
  - RI
- 가장 비쌈 (실제 물리 서버라서..)

Dedicated Instances
- 전용 하드웨어에서 실행되는 인스턴스(물리적 서버랑은 좀 다름)
- 같은 계정 다른 하드웨어랑 공유하기도 하는데 인스턴스 배치는 바꿀 수 없음..

Dedicated Hosts vs Dedicated Instances
- Instance : 사용자 하드웨어에 고유한 인스턴스를 갖는 것
- Hosts : 물리적 서버 자체에 액세스 해서 저수준 하드웨어에 대한 가시성을 제공함

RI vs Savings Plan
- RI는 지역, 크기, 인스턴스 패밀리를 정하면 거의 변경이 불가능
- Savings Plan은 특정 인스턴스 패밀리의 일정 비용을 지불하겠다 약정하여 할인 받는 가격모델
- Savings Plan은 한 번 구입하면 재판매, 전호나 불가능(RI는 가능)

Capacity Reservations
- 원하는 기간 동안 특정 AZ에 온디멘드 인스턴스 예약 가능 -> 이후 필요할 때 마다 그 용량에 액세스 가능
- 시간 약정이 없기 때문에 언제든 용량 예약하거나 취소 가능
- 다만 사용 안해도 시간마다 비용은 지불됨...

** AZ vs Region
- AZ(Availability Zone) : 가용영역 (ex. north-"a", north-"b" 처럼 리전 내에서 나뉘어지는 영역)
- Region : 물리적인 영역 (ex. "north"-a, "north"-b)

## IPv4 요금
- 24년 2월 1일부터 계정에 생성된 모든 Public IPv4에 대해 사용 여부와 관계 없이 과금됨(시간당 $0.005...)
- IPv6는 요금 없음 (AWS에서 IPv6로 전환시키기 위함....)


## QnA
EC2 인스턴스 안팎의 트래픽을 제어하려면 무엇을 사용해야 할까요?
- 보안그룹 (인스턴스 수준에서 작동하며 트래픽을 컨트롤 가능)

여러분은 몇 개의 EC2 인스턴스에서 호스팅될 애플리케이션을 시작할 준비를 하고 있습니다. 이 앱은 일부 소프트웨어 설치가 필요하고 일부 OS 패키지는 처음 실행 시 업데이트해야 합니다. EC2 인스턴스를 시작할 때 이를 달성하는 가장 좋은 방법은 무엇일까요?
- 사용자 데이터 활용