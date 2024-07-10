const form = document.getElementById("Hello")
form.addEventListener("submit", function(event) {
    event.preventDefault()
    let formdata = new FormData(form)
    fetch("/form", {method: "POST", body: formdata})
})