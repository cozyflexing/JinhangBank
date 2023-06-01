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
        case "v":
            document.querySelector(".quitItemEnterPin button").click();
            break;
    }
}

setInterval(pollArduino, 200);  // poll every second
