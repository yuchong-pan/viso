editor.setReadOnly(true);

var socket = io.connect("http://viso.hackinit.io/LP01632947305");
socket.on("modify", function(data) {
    if (editor.getValue() != data) {
        editor.setValue(data, 0);
    }
});
