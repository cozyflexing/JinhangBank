function pollArduino() {
    fetch("/arduinoInput")
        .then(response => response.json())
        .then(data => {
            let button_pressed = data.button_pressed;
            if (button_pressed) {
                triggerButtonOtherAmount(button_pressed);
            }
        });
}
function triggerButtonOtherAmount(button) {
    let pinCodeInput = document.getElementById('other_amount');
    switch (button) {
        case "0":
            pinCodeInput.value += '0';
            break;
        case "1":
            pinCodeInput.value += '1';
            break;
        case "2":
            pinCodeInput.value += '2';
            break;
        case "3":
            pinCodeInput.value += '3';
            break;
        case "4":
            pinCodeInput.value += '4';
            break;
        case "5":
            pinCodeInput.value += '5';
            break;
        case "6":
            pinCodeInput.value += '6';
            break;
        case "7":
            pinCodeInput.value += '7';
            break;
        case "8":
            pinCodeInput.value += '8';
            break;
        case "9":
            pinCodeInput.value += '9';
            break;
        case "e":  // Submit button
            document.querySelector('.enterAmountForm form').submit();
            break;
        case "d":  // Delete button
            pinCodeInput.value = pinCodeInput.value.slice(0, -1);  // Remove the last character
            break;
        case "c":  // Cancel button
            pinCodeInput.value = '';  // Clear the input field
            break;
    }
}

setInterval(pollArduino, 100);