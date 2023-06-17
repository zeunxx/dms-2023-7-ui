## 📲 Kaftalk

2023 건국대학교 분산시스템및컴퓨팅 프로젝트

kafka와 flask를 사용한 단체 채팅 어플리케이션 서비스 

1. Kafka 클러스터 구성 : Kafka 클러스터를 구성하고, 브로커를 배치하여 분산 처리 환경을 확보한다. 

2. 채팅방 생성 및 관리: 사용자는 생성된 채팅방에 참여할 수 있고, 나갈 수 있다. 

3. 메시지 전송 : 사용자는 웹 인터페이스를 통해 메시지를 입력하고, 해당 채팅방에 있는 다른 사람들에게 메시지를 전송할 수 있다. 

4. Kafka 메시지 스트림 : 사용자가 메시지를 전송하면, Kafka는 해당 메시지를 스트림으로 생성하고, 해당 채팅방의 모든 사용자들에게 메시지를 분산처리 한다. 

5. 웹 클라이언트 인터페이스 : 사용자는 웹 브라우저를 통해 채팅방에 접속하고, 실시간으로 메시지를 주고받을 수 있는 웹 클라이언트 인터페이스를 통해 서비스를 이용할 수 있다. 

<br>

|역할 분담|학번|설명|
|------|---|---|
|박지은|202015007| kafka server와 chatting server 개발 및 배포, 단체 채팅 개발(kafka 이용), 이미지 전송 개발(s3, lambda 이용)|
|이지영|202012316|kafka server와 chatting server 개발 및 배포, 방해금지모드 개발 (배치 처리 이용)|
|이의석|202372193|발표 자료 작성, UI 개발|

<br>


### 💡 요구사항

<img width="367" alt="image" src="https://github.com/zeunxx/dms-2023-7-project/assets/81572478/cd1707e5-33a9-4083-95fa-38d9e6b22f1f">

- 단체 채팅 

- 특정 시간 방해 금지 기능 

- 파일 전송 기능 - 이미지 혹은 음성 데이터 전송

  <br>

  

### 💡  아키텍처 


<img width="700" alt="image" src="https://github.com/zeunxx/dms-2023-7-project/assets/81572478/2bdce7dd-e617-4488-b4cd-4b0346aba812">

<br>

####  1️⃣ logical sw architecture

<img width="500" alt="image" src="https://github.com/zeunxx/dms-2023-7-project/assets/81572478/bf838967-0f05-4c7d-b05a-849c70a7fb17">

<br>

####  2️⃣ class diagram
<img width="450" alt="image" src="https://github.com/zeunxx/dms-2023-7-project/assets/81572478/11e2aa85-f8e3-473f-92bd-7a4aded50eb4">






<br>

 #### 📌 서버 주소
- kafka server : http://3.135.130.17:8989/
- ui server : http://18.221.31.141:5000/
