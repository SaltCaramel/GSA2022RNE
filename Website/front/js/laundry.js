function laundry(){
    fetch("http://10.59.14.61:5000/laundrycheck")
    .then((response) => {
       // console.log(`response!!! =  ${response}`)
        return response
    })
}  