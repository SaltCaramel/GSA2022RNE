const { Router, request } = require('express');
const express=require('express');
const app=express();
//Aruduino
const http = require('http'); 
const server = http.createServer(app); 
const { Server } = require("socket.io"); 
const io = new Server(server);

/*
// public 폴더하위의 파일들을 기본으로 서비스
app.use(express.static('front'));

// 페이지를 찾을 수 없음 오류 처리
app.use(function(req, res, next) {
    res.status(404);	
    res.send(
		'<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">' +
		'<html><head><title>404 페이지 오류</title></head>' + 
		'<body><h1>찾을 수 없습니다</h1>' + 
		'<p>요청하신 URL ' + req.url + ' 을 이 서버에서 찾을 수 없습니다..</p><hr>' +
		'</body></html>'
	);
});
app.listen(8080, function() {});
*/

// localhost:3000으로 방문 시 index.html로 라우팅
app.get('/', (req, res) => { res.sendFile(__dirname + '/Arduino.html'); }); 
// socket이 connection 상태일때 
io.on('connection', (socket) => { 
	console.log('연결');
	socket.on('chat message', (msg) => { 
    	io.emit('chat message', msg); 
        console.log('message: ' + msg); 
        }
    );
socket.on('disconnect', () => {
	console.log('user disconnected');
    });
});

// server는 localhost:3000
server.listen(3000, () => {
	console.log('listening on *:3000'); 
});






