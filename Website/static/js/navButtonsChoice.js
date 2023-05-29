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
            document.querySelector(".quitItemEnterPin button").click();
            break;
        case "5":
            document.querySelector(".showBalanceForm button").click();
            break;
        case "6":
            document.querySelector(".withdrawMoneyForm button").click();
            break;
        case "7":
            document.querySelector(".changePinForm button").click();
            break;
        case "8":
            document.querySelector(".pickLanguageItem button").click();
            break;
    }
}

setInterval(pollArduino, 100);  // poll every second
