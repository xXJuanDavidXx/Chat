$(function() {
	
	
	//Obteniendo la url del proyecto para la comunicación sockets
	
	var url = 'ws://' + window.location.host + '/ws/room/' + roomId + '/'
	
	console.log(url)

	//Creando comunicación websocket
	
	var chatSocket = new WebSocket(url)
	
	chatSocket.onopen = function(e){
		console.log("WEBSOCKET OPEN")
	}

	chatSocket.onclose = function(e){
		console.log("Cerrado")
	}


    // Configurando el evento de enviar la información ya sea por click o presionando la tecla enter
    document.querySelector('#btnMessage').addEventListener('click', sendMessage);

    document.querySelector('#inputMessage').addEventListener('keypress', function(e) {
        if (e.keyCode == 13) {
            sendMessage();
        }
    });

    // Configurando la función que envía el mensaje y limpia el input cada que se envía
    function sendMessage() {
        var message = document.querySelector('#inputMessage');

        loadMessageHTML(message.value.trim());

        if (message.value.trim() !== '') {
            message.value = '';
        }
    }

    // Cómo se muestra el mensaje que envió el usuario
    function loadMessageHTML(m) {
        document.querySelector('#boxMessage').innerHTML +=
        `
        <div class="alert alert-primary" role="alert">
            ${m}
            <div>
                <small class="fst-italic fw-bold"> ${usuario} </small>
                <small class="float-end">0000444000</small>
            </div>
        </div>
        `;
    }

});

