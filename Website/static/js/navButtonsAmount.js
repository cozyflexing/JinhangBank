function pollArduino() {
    fetch("/arduinoInput")
        .then(response => response.json())
        .then(data => {
            let button_pressed = data.button_pressed;
            if (button_pressed) {
                triggerButton(button_pressed);
            }
        });
}

function triggerButton(button) {
    switch (button) {
        case "1":
            document.querySelector(".goBackItem button").click();
            break;
        case "2":
            document.querySelector(".chooseAmount20 button").click();
            break;
        case "3":
            document.querySelector(".chooseAmount50 button").click();
            break;
        case "4":
            document.querySelector(".quitItemChooseAmount button").click();
            break;
        case "5":
            document.querySelector(".chooseAmount70 button").click();
            break;
        case "6":
            document.querySelector(".chooseAmount100 button").click();
            break;
        case "7":
            break;
        case "8":
            document.querySelector(".otherAmount button").click();
            break;
    }
}

setInterval(pollArduino, 100);  // poll every second
