var submitEmailBtn
var userName
var userEmail
var emailSubject
var emailMessage

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', (event) => {
        submitEmailBtn = document.getElementById("submitEmail")
        makeEvenListner()
    })
} else {
    submitEmailBtn = document.getElementById("submitEmail")
    makeEvenListner()
}

function makeEvenListner() {
    console.log("entered makeEvenListener")
    submitEmailBtn.addEventListener("click", validateForm)
}

function validateForm() {
    console.log("entered validateForm")
    //TODO Validate
}