// script.js
window.onload = function() {
    setInterval(function() {
        fetch('/poll_for_card') // New endpoint that will return the card info
            .then(response => response.json())
            .then(data => {
                if (data.pas_nummer) {
                    // Redirect to verifyPasNummer route with card number
                    window.location.href = '/verifyPasNummer?pas_nummer=' + data.pas_nummer;
                }
            });
    }, 5000); // Check every 5 seconds
};
