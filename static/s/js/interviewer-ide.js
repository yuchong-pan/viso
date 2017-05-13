editor.setReadOnly(true);

var socket = io.connect("http://viso.hackinit.io/LP01632947305");
socket.on("modify", function(data) {
    body = JSON.parse(data);
    editor.setValue(body["code"]);
    editor.moveCursorToPosition(body["pos"]);
    editor.clearSelection();
    for (i in body["select"]) {
        editor.addSelectionMarker(i);
    }
});
