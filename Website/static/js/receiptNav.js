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
        case "v":
            document.querySelector(".noReceipt button").click();
            break;
        case "z":
            document.querySelector(".yesReceipt button").click();
            break;
    }
}

setInterval(pollArduino, 100);  // poll every second
