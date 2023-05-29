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
            break;
        case "3":
            break;
        case "4":
            document.querySelector(".quitItem button").click();
            break;
        case "5":
            document.querySelector(".nederlandsItem button").click();
            break;
        case "6":
            document.querySelector(".deutschItem button").click();
            break;
        case "7":
            document.querySelector(".francaisItem button").click();
            break;
        case "8":
            document.querySelector(".englishItem button").click();
            break;
    }
}

setInterval(pollArduino, 100);  // poll every second
