## TCP/IP

* 정의
  - 네트워크 프로토콜의 모음으로 패킷 통신 방식의 IP와 전송 조절 프로토콜인 TCP로 이루어져 있다.

## TCP/IP 7Model

  1. Network Interfact, 물리 계층으로 네트워크 노드들을 상호 연결
  2. Network, 패킷을 처리하고 다른 네트워크와 연결
  3. Transport, TCP/UDP
  4. Applicaiton, 응용 프로그램간 표준화 된 데이터 교환

## 인캡슐레이션

  1. Application                      HostData
  2. Presentation                     
  3. Session                          Data          
  4. Transport (Segment)   TcpHeader Data   
  5. Network  (Packet)     IpHeader Data
  6. DataLink (Frame)      MAC LLC Header Data FCS
  7. Physical (bit)       Signal 101010101010101010

## 디캡슐레이션 

인캡슐레이션의 반대로 진행

* 캡슐화를 통해서 네트워크는 통신한다