# EC2 인스턴스 스토리지
## EBS
EBS(Elastic Block Store)란
- 인스턴스가 실행중인동안 연결 가능한 네트워크 드라이브
- 인스턴스가 종료된 후에도 데이터를 지속할 수 있음
  - 인스턴스 재생성하고 EBS 마운트만 하면 이전 데이터로 다시 볼륨을 생성할 수 이씅ㅁ
- EBS볼륨 레벨
  - CCP 레벨 : 하나의 EBS는 하나의 EC2에만 마운트 가능
  - 어소시에이트 레벨 : 일부 EBS 다중 연결
- EBS볼륨은 특정 가용영역에 속해있음
  - EBS볼륨이 us-east-1a에서 생성된 경우에는 us-east-1b에는 연결 불가능
- 네트워크 USB 스틱이다~ -> 실물 USB는 아니지만 가상의 USB로 이컴퓨터 저컴퓨터에 연결하는 고런 데이터저장용 하드웨어...
- Free tire : 30GB의 EBS storage(범용 SSD) 혹은 Magnetic per month 
- **물리적 드라이브**
  - EC2와 EBS를 연결하기 위해서는 네트워크가 필요함. 네트워크가 사용되기 때문에 지연이 생길 수 있음
  - EC2인스턴스에서 분리될 수 있고 다른 인스턴스에 연결할 수 있음
- 특정 가용영역(AZ, Availability Zone)에 고정되어 있으므로 다른 영역에 도달할 수 없음
  - 다만 snapshot을 이용하면 다른 가용역역으로도 볼륨을 옮길 수 있음
- 용량을 미리 정해야함(GBs, IOPS)
  - 추후 변경 가능
- 하나의 EBS가 여러 EC2에 연결은 불가능. 하나의 EC2에 여러 EBS는 연결 가능

종료 시 삭제
- EC2 생성할 때 Delete on Termination 을 체크하면 EC2 삭제 시 EBS를 함께 삭제할 수 있음

EBS Snapshots Feature
- EBS Snaptshot Archive
  - 스냅샷을 최대 75%저렴한 아카이브 티어로 옮기는 방법
  - 아카이브 티어로 옮기면 24~72시간 정도가 걸림
- Recycle Bin for EBS Snapshots
  - 스냅샷을 영구적으로 삭제하는 대신 휴지통으로 이동. 휴지통 보관 기간은 1일~1년까지 설정가능
- Fast Snapshot Restore(FSR)
  - 스냅샷을 완전히 초기화 하는 것
  - 비용이 많이 들기 때문에 조심해야함

## EFS(Elastic File System)
- NFS(network file system)으로, 여러 EC2에 마운트 될 수 있음
- 여러 AZ에 있는 EC2에서도 동작함
- 고가용성, 스케일가능, 비쌈... -> 사용량에 따라 비용을 지불하기 때문에 미리 비용을 지정할 필요가 없음

사용사례
- 콘텐츠관리, 웹서비, 데이터 공유, 워드프레스 등...
- NFS프로토콜을 이해해야함
- 리눅스 기반 AMI와만 호환됨

