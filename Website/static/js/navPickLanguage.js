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
            document.querySelector(".quitItem button").click();
            break;
        case "w":
            document.querySelector(".nederlandsItem button").click();
            break;
        case "x":
            document.querySelector(".deutschItem button").click();
            break;
        case "y":
            document.querySelector(".francaisItem button").click();
            break;
        case "z":
            document.querySelector(".englishItem button").click();
            break;
    }
}

setInterval(pollArduino, 100);  // poll every second
