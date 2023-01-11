const roomName = JSON.parse(document.getElementById('room-name').textContent);
const currentUser = JSON.parse(document.getElementById('current-user').textContent);
const debugMode = JSON.parse(document.getElementById('debug-mode').textContent);

const chatSocket = debugMode == 0 ? new WebSocket('ws://' + window.location.host + '/ws/chat/' + roomName + '/') :
 new WebSocket('wss://' + window.location.host + '/ws/chat/' + roomName + '/');

chatSocket.onopen = function (e) {
    console.log("websocket connection is successful")
};

chatSocket.onclose = function (e) {
    console.log('websocket closed unexpectedly')
};

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    window.scroll(0, 3000);
    // create html element with class attributes
    var receivedMessage = document.createElement("p");
    var sentMessage = document.createElement("p");
    var flexEndDiv = document.createElement("div");
    var flexStartDiv = document.createElement("div");
    // add attributes to the created elements
    receivedMessage.classList.add("text-white", "p-1", "px-2", "rounded", "receive");
    sentMessage.classList.add("text-white", "p-1", "px-2", "rounded", "sent");
    flexEndDiv.classList.add("d-flex", "justify-content-end", "ml-10");
    flexStartDiv.classList.add("d-flex", "justify-content-start", "mr-10");

    sentMessage.innerHTML = data.message;
    receivedMessage.innerHTML = '<small>' + data.username + '</small>' + ' <br> ' + data.message;

    flexStartDiv.appendChild(receivedMessage);
    flexEndDiv.appendChild(sentMessage);

    document.querySelector('#input-message').value = "";
    if (data.username == currentUser) {
        document.getElementById('messages').appendChild(flexEndDiv)

    } else {
        document.getElementById('messages').appendChild(flexStartDiv)
    }

};

document.getElementById('input-message').onkeyup = function (e) {
    if (e.keyCode === 13) {
        document.getElementById('message-send').click();
    }
};
document.getElementById('input-message').focus();
document.getElementById('message-send').onclick = function (e) {
    var messageInput = document.getElementById('input-message').value;
    var username = currentUser
    chatSocket.send(JSON.stringify({ username: username, message: messageInput }));
};


window.onload = function (e) {
    window.scroll(0, 2500);
}
