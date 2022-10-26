import fetch from "node-fetch";

var res;

fetch("http://127.0.0.1:5000/query/"+"봉사활동 시간 알고싶어")
.then((response) => response.json())
.then((data) => {
    res = String(data['Answer']);
    console.log(res);
})