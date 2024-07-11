const form = document.getElementById("Hello")
const btn_logout = document.getElementById("logout")

btn_logout.onclick = logout;

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

