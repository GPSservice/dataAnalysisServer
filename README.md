[2021/09/03 update] (junsang)

- 서버 프레임워크 express -> flask로 변경 
(Kmeans구현한게 python이기 때문에 편의를 위해서 python framework인 flask 사용)
- structure
    - [ / ] application.py가 루트 페이지 
    - [ /getJson ] / 에서 "버튼 한번 눌러보슈"버튼을 누르면 Kmeans수행 후 resultJSON.json에 파일로 저장
    - [ /jsonread ] resultJSON.json에 저장된 데이터를 읽어 rendering해줌 (AppServer에서는 이곳에 접근하여 데이터를 받음)


<br>
[2021/08/24 update] (junsang)

- index.js -> GET/getjson에 있는 jsonData변수가 resultJSON파일을 그대로 읽은 것 ===> 웹 브라우저에서는 index.js의 버튼을 누르면 데이터가 그대로 뜸
- 혹시 몰라서 JSON output data 파일 추가 (resultJSON.json) ==> 잘 안되면 직접 파일에 접근해서 진행할 것
- DELETE gpsservice.sql

<br>
[2021/08/21 update] (junsang)

- gpsservice.sql을 local DB에 저장한 후 local DB에서 처리
- index.js -> getJson()에 있는 jsonData변수가 DB에 있던 input JSON데이터를 저장한 것
- localhost로 실행하면 됨