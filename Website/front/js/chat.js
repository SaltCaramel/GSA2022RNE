function qna(){
    var v1 = String(document.getElementById("dataInput").value);
    
    fetch("http://127.0.0.1:5000/query/"+v1)
    .then((response) => {
        console.log(`response!!! =  ${response}`)
        return response.json()
    })
    .then((data) => {
        console.log(`data = ${data}`)
        res = String(data['Answer']);
        document.getElementById("res").value = res;
    })
}  