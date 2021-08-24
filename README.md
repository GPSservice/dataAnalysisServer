[2021/08/24 update] (junsang)

- JSON output data 파일 추가 (resultJSON.json)
    => 우선 이걸로 작업하고 나중에 AWS올려지면 그떄 jsonFile -> jsonData변환 작업 빼주면 됨
- DELETE gpsservice.sql

[2021/08/21 update] (junsang)

- gpsservice.sql을 local DB에 저장한 후 local DB에서 처리
- index.js -> getJson()에 있는 jsonData변수가 DB에 있던 input JSON데이터를 저장한 것
- localhost로 실행하면 됨