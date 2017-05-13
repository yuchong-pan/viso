var socket = io.connect("http://viso.hackinit.io/LP01632947305");
socket.on("modify", function(data) {
    editor.setValue(data, 0);
});
editor.on("change", function() {
    Vue.http.post("http://viso.hackinit.io/api/ide/modify", {
        "code": editor.getValue(),
        "author": "LP01632947305"
    });
});
