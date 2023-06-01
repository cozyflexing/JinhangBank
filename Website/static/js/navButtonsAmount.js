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
        case "s":
            document.querySelector(".goBackItem button").click();
            break;
        case "t":
            document.querySelector(".chooseAmount20 button").click();
            break;
        case "u":
            document.querySelector(".chooseAmount50 button").click();
            break;
        case "v":
            document.querySelector(".quitItemChooseAmount button").click();
            break;
        case "w":
            document.querySelector(".chooseAmount70 button").click();
            break;
        case "x":
            document.querySelector(".chooseAmount100 button").click();
            break;
        case "z":
            document.querySelector(".otherAmount button").click();
            break;
    }
}

setInterval(pollArduino, 200);  // poll every second
