const form = document.getElementById("Hello")
const btn_logout = document.getElementById("logout")
const username_display = document.getElementById("username")
const first_latter = document.getElementById("firstLatter")


btn_logout.onclick = logout;

document.addEventListener("DOMContentLoaded", function () {
    fetch("/display_username", {method: "GET"}).then(response => response.json()).then(function (data) {
        username_display.innerText = data.username;
        first_latter.innerText = data.username[0].toUpperCase()
    })
})

form.addEventListener("submit", function(event) {
    event.preventDefault()
    let formdata = new FormData(form)
    fetch("/form", {method: "POST", body: formdata})
})

function logout() {
    fetch("/logout", {method:"GET"}).then(response => response.json()).then(function (data) {
        if (data.success === true) {
            window.location.href = "/";
        }
    })
}
