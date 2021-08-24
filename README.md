[2021/08/24 update] (junsang)

- index.js -> GET/getjson에 있는 jsonData변수가 resultJSON파일을 그대로 읽은 것
    ===> 웹 브라우저에서는 index.js의 버튼을 누르면 데이터가 그대로 뜸
- 혹시 몰라서 JSON output data 파일 추가 (resultJSON.json)
        ==> 잘 안되면 직접 파일에 접근해서 진행할 것
- DELETE gpsservice.sql

[2021/08/21 update] (junsang)

- gpsservice.sql을 local DB에 저장한 후 local DB에서 처리
- index.js -> getJson()에 있는 jsonData변수가 DB에 있던 input JSON데이터를 저장한 것
- localhost로 실행하면 됨