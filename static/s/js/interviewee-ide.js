var socket = io.connect("http://viso.hackinit.io/interviewee");
editor.on("change", function() {
    window.setTimeout(function() {
        Vue.http.post("http://viso.hackinit.io/api/ide/modify", {
            "code": editor.getValue(),
            "pos": editor.getCursorPosition(),
            "select": editor.getSelection().rangeList.ranges
        });
    }, 50);
});

function setLang(lang) {
    editor.getSession().setMode("ace/mode/" + lang);
    Vue.http.get("http://viso.hackinit.io/api/ide/lang?l=" + lang);
}
