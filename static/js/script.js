document.addEventListener("DOMContentLoaded", function () {
    const contactForm = document.getElementById("survey-form");
    const responseMessage = document.getElementById("responseMessage");
    const overlay = document.getElementById("overlay");
    const close_button = document.getElementById("close_button");

    close_button.addEventListener("click", function (event) {
        responseMessage.innerHTML = "";
        overlay.classList.remove("show")
        responseMessage.classList.remove("success", "show");
    })
    
    contactForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const no_of_preg = document.getElementById('no_of_preg').value;
        const Glucose = document.getElementById('Glucose').value;
        const BloodPressure = document.getElementById('BloodPressure').value;
        const SkinThickness = document.getElementById('SkinThickness').value;
        const Insulin = document.getElementById('Insulin').value;
        const BMI = document.getElementById('BMI').value;
        const DiabetesPedigreeFunction = document.getElementById('DiabetesPedigreeFunction').value;
        const Age = document.getElementById('Age').value;
        
        

        // const formData = new FormData(contactForm);
        const formData = {
            no_of_preg: no_of_preg,
            Glucose: Glucose,
            BloodPressure: BloodPressure,
            SkinThickness: SkinThickness,
            Insulin: Insulin,
            BMI: BMI,
            DiabetesPedigreeFunction: DiabetesPedigreeFunction,
            Age: Age,
        };

        const apiEndpoint = "/predict";

        fetch(apiEndpoint, {
            method: "POST",
            headers: {
                'Content-Type':
                    'application/json;charset=utf-8'
            },
            body: JSON.stringify(formData)
        })
            .then(response => response.json())
            .then(data => {
                if(data.Ok == "True"){
                    if(data.pred == "1")
                        responseMessage.innerHTML = `<p>You have Diabetes</p>`;
                    else
                        responseMessage.innerHTML = `<p>You don't have Diabetes</p>`;
                }
                else {
                    responseMessage.innerHTML = `<p>${data.error}</p>`;
                }
                console.log(data)
                overlay.classList.add("show")
                responseMessage.classList.add("success", "show"); // Add 'show' class to make the message visible
            })
            .catch(error => {
                console.error("Error:", error);
                responseMessage.innerHTML = `<p>Error submitting the form. Please try again later.</p>`;
                responseMessage.classList.add("error", "show"); // Add 'show' class to make the message visible

                setTimeout(() => {
                    responseMessage.innerHTML = "";
                    responseMessage.classList.remove("error", "show");
                }, 23000);
            });
    });
});