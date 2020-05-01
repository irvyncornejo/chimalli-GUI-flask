const socket = io()

socket.emit('data', (data_read) =>{
    document.getElementById('dataSensor').innerHTML += `<p> ${data_read} </p>`
})

//Escuchador de los eventos que vienen desde el servidor
socket.on('message', (msg) =>{
    document.getElementById('dataSensor').innerHTML = `<li> ${msg} </li>`
})

function sendMessage(){
    const message = document.getElementById('myMessage').value
    //Envio de mensaje a todos los clientes
    socket.send(message)
    document.getElementById('myMessage').value = ''
}
