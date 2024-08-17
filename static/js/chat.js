window.onload = function() {
    document.querySelector('#btnMessage').addEventListener('click', sendMessage)

    document.querySelector('#inputMessage').addEventListener('keypress', function(e) {
        if (e.keyCode == 13) {
            sendMessage()
        }
    })

    function sendMessage() {
        var message = document.querySelector('#inputMessage')

        loadMessageHTML(message.value.trim())

        if (message.value.trim() !== '') {
            message.value = ''
        }
    }

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
        `
    }
}

