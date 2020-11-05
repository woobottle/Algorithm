# ACL(Access Control List)

[1.acl 정의](#acl-정의)
[2.acl 기능](#acl-기능)
[3.acl 종류](#acl-종류)

## acl 정의
* 트래픽 필터링과 방화벽을 구축하는데 가장 중요한 요소, 허가되지 않은 이용자를 차단하는것 

## acl 기능
* 내부적인 패킷 필터링
* 부적절한 인터넷 접근으로부터의 내부 네트워크 보호
* 가상 터미널 포트들에 대한 접근 제한

## acl 종류
1. Standard
- 기본적인 엑세스 제어, IP Packet의 출발지 주소(Source Address)만 검사하여 제어, L3 장비에서 적용

2. Extended
- IP Packe의 source, destination, Protocol을 검사하여 제어하며, L3 장비에서 적용
- 특정 프로토콜, 포트번호 등 여러 매개 변수 사용 


출처: https://touo.tistory.com/43