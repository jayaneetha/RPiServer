const BASE_URL = "http://192.168.20.5:8000";
var xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function () {
    if (this.readyState === 4) {
        console.log(this.responseText);
    }
});


document.getElementById("btnF").addEventListener("click", () => {
    xhr.open("GET", BASE_URL + "/forward");
    xhr.send();
})

document.getElementById("btnL").addEventListener("click", () => {
    xhr.open("GET", BASE_URL + "/left");
    xhr.send();
})

document.getElementById("btnR").addEventListener("click", () => {
    xhr.open("GET", BASE_URL + "/right");
    xhr.send();
})

document.getElementById("btnB").addEventListener("click", () => {
    xhr.open("GET", BASE_URL + "/backward");
    xhr.send();
})

document.getElementById("btnS").addEventListener("click", () => {
    xhr.open("GET", BASE_URL + "/stop");
    xhr.send();
})


document.getElementById("speed").addEventListener("change", (el) => {
    const val = el.target.value
    document.getElementById("lblSpeed").innerText = "Speed : " + val;
    xhr.open("POST", BASE_URL + "/speed?speed=" + val);
    xhr.send();
})


