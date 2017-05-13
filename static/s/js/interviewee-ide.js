var socket = io.connect("http://viso.hackinit.io/interviewee");
editor.on("change", function() {
    if (editor.getValue() != "") {
        Vue.http.post("http://viso.hackinit.io/api/ide/modify", {
            "code": editor.getValue(),
            "pos": editor.getCursorPosition(),
            "select": editor.getSelection().rangeList.ranges
        });
    }
});
