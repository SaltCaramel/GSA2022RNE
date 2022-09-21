const express=require('express');
const app=express();

// public 폴더하위의 파일들을 기본으로 서비스
app.use(express.static('front'));

app.listen(8080, function() {});