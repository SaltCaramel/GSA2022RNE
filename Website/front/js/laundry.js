  function laundry(){
    fetch("http://10.82.119.182:5000/laundrycheck")
    .then((response) => {
        console.log(`response!!! =  ${response}`)
        return response.json()
    })
    .then((data) => {
        console.log(`data = ${data}`)
        laun = res = String(data['laundry']);;
        document.getElementById("laun").value = laun;
    })
}  