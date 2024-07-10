const form = document.getElementById("login_form")
const buttonSingUp = document.getElementById("button_sing")
const button_submit = document.getElementById("loginformsubmit")

buttonSingUp.onclick = changeToSingUp;

form.addEventListener("submit", function (event) {
    event.preventDefault();
    if (buttonSingUp.innerText === "sing up" || buttonSingUp.innerText === "Sing up"){
        login();
    } else {
        singup();
    }
})

function login() {
    let formdata = new FormData(form);
    fetch("/login", {method: "POST", body: formdata}).then(response => response.json()).then(function (data) {
        if (data.success === true) {
            window.location.href = "/";
        }
    });
}

function changeToSingUp() {
    button_submit.innerText = "Sing Up"; 
    buttonSingUp.innerText = "Login";
    buttonSingUp.onclick = changeToLogin;
}

function changeToLogin() {
    button_submit.innerText = "Login";
    buttonSingUp.innerText = "Sing up";
    buttonSingUp.onclick = changeToSingUp;
}

function singup() {
    let formdata = new FormData(form);
    fetch("/Singup", {method: "POST", body:formdata});
    changeToLogin();
}

