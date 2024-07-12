const form = document.getElementById("login_form")
const buttonSingUp = document.getElementById("button_sing")
const button_submit = document.getElementById("loginformsubmit")
const login_div = document.getElementById("login_div")

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
        } else {
            error_div(data.error);
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

function error_div(thingThatWentWrong) {
    cleanTheErrors();
    let error_div = document.createElement("div");
    error_div.className = "error_div";
    error_div.id = "error_div";
    let h3_error = document.createElement("h3");
    h3_error.innerText = thingThatWentWrong;
    h3_error.className = "error_h3";
    error_div.appendChild(h3_error);
    login_div.appendChild(error_div);
}


function cleanTheErrors() {
    let divToRemove = document.getElementById("error_div");
    console.log(divToRemove)
    if (divToRemove) {
        login_div.removeChild(divToRemove);
    }
}