const express = require("express")
const app = express()
const port = 3000
app.listen(port, ()=> {
    console.log("localhost 서버 실행중")
})
app.engine("html", require("ejs").renderFile);
app.set("view engine", "html")
////// express 구축 /////

//import 구간//
const jsonGet = require("./modules/getJson")
//////////////

app.get('/', (req, res) => {
    res.render("button.html")
    //관리자 페이지 작성
})

app.get('/getJson', async (req, res) => {
    const jsonData = await jsonGet.jsonGetquery().then();
    console.log("jsonData: ", jsonData[0]);
    res.send(jsonData);
})