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
            break;
        case "2":
            break;
        case "3":
            break;
        case "4":
            break;
        case "5":
            break;
        case "6":
            break;
        case "7":
            break;
        case "8":
            document.querySelector(".pickLanguageItem button").click();
            break;
    }
}

setInterval(pollArduino, 100);  // poll every second
