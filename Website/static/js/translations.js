// translations.js

const translations = {
    en: {
        scanCard: 'Scan Your Card',
        neverShare: 'Never your pin with others',
        quit: "Quit",
        enterPin: "Enter your pin",
        pressOK: "Press OK to continue",
        makeAChoice: "Make a choice",
        showBalance: "Show balance",
        withdrawMoney: "Withdraw money",
        changePin: "Change pin",
        chooseYourLanguage: "Choose your language",
        blockedCard: "Your card has been blocked",
        contactBank: "Please contact your bank...",
        otherAmount: "Other amount",
        pickAmount: "Pick an amount",
        yourBalance: "Your balance:",
        newPin: "Enter a new pin",
        bye: "Good bye",
        unavailable: "The amount you have picked is not available",
        enterAmount: "Enter desired amount:",
        minimalTen: "Minimal €10",
        pleaseBePatient: "Please be patient",
        takeYourMoney: "Take your money from the drawer",
        wantReceipt: "Do you want a receipt?",
        yes: "Yes",
        no: "No",
        takeYourReceipt: "Take your receipt please",
        goBack: "Go Back",
    },
    fr: {
        scanCard: 'Scannez votre carte',
        neverShare: 'Ne partagez jamais votre code avec les autres',
        quit: "Quitter",
        enterPin: "Entrez votre code",
        pressOK: "Appuyez sur OK pour continuer",
        makeAChoice: "Faites un choix",
        showBalance: "Afficher le solde",
        withdrawMoney: "Retirer de l'argent",
        changePin: "Changer de code",
        chooseYourLanguage: "Choisissez votre langue",
        blockedCard: "Votre carte a été bloquée",
        contactBank: "Veuillez contacter votre banque...",
        otherAmount: "Autre montant",
        pickAmount: "Choisissez un montant",
        yourBalance: "Votre solde:",
        newPin: "Entrez un nouveau code",
        bye: "Au revoir",
        unavailable: "Le montant que vous avez choisi n'est pas disponible",
        enterAmount: "Entrez le montant souhaité:",
        minimalTen: "Minimum €10",
        pleaseBePatient: "Veuillez patienter",
        takeYourMoney: "Prenez votre argent dans le tiroir",
        wantReceipt: "Voulez-vous un reçu?",
        yes: "Oui",
        no: "Non",
        takeYourReceipt: "Prenez votre reçu s'il vous plaît",
        goBack: "Retour",
    },
    nl: {
        scanCard: 'Scan uw kaart',
        neverShare: 'Deel uw pincode nooit met anderen',
        quit: "Afsluiten",
        enterPin: "Voer uw pincode in",
        pressOK: "Druk op OK om door te gaan",
        makeAChoice: "Maak een keuze",
        showBalance: "Toon saldo",
        withdrawMoney: "Geld opnemen",
        changePin: "Pincode wijzigen",
        chooseYourLanguage: "Kies uw taal",
        blockedCard: "Uw kaart is geblokkeerd",
        contactBank: "Neem contact op met uw bank...",
        otherAmount: "Ander bedrag",
        pickAmount: "Kies een bedrag",
        yourBalance: "Uw saldo:",
        newPin: "Voer een nieuwe pincode in",
        bye: "Tot ziens",
        unavailable: "Het door u gekozen bedrag is niet beschikbaar",
        enterAmount: "Voer gewenst bedrag in:",
        minimalTen: "Minimaal €10",
        pleaseBePatient: "Gelieve geduldig te zijn",
        takeYourMoney: "Neem uw geld uit de lade",
        wantReceipt: "Wilt u een ontvangstbewijs?",
        yes: "Ja",
        no: "Nee",
        takeYourReceipt: "Neem uw ontvangstbewijs alstublieft",
        goBack: "Ga terug",
    },
    de: {
        scanCard: 'Karte scannen',
        neverShare: 'Teilen Sie Ihre PIN niemals mit anderen',
        quit: "Beenden",
        enterPin: "Geben Sie Ihre PIN ein",
        pressOK: "Drücken Sie OK, um fortzufahren",
        makeAChoice: "Treffen Sie eine Auswahl",
        showBalance: "Kontostand anzeigen",
        withdrawMoney: "Geld abheben",        
        changePin: "PIN ändern",
        chooseYourLanguage: "Wählen Sie Ihre Sprache",
        blockedCard: "Ihre Karte wurde gesperrt",
        contactBank: "Bitte wenden Sie sich an Ihre Bank...",
        otherAmount: "Anderer Betrag",
        pickAmount: "Wählen Sie einen Betrag",
        yourBalance: "Ihr Kontostand:",
        newPin: "Geben Sie eine neue PIN ein",
        bye: "Auf Wiedersehen",
        unavailable: "Der von Ihnen gewählte Betrag ist nicht verfügbar",
        enterAmount: "Gewünschten Betrag eingeben:",
        minimalTen: "Mindestens €10",
        pleaseBePatient: "Bitte haben Sie Geduld",
        takeYourMoney: "Nehmen Sie Ihr Geld aus der Schublade",
        wantReceipt: "Möchten Sie eine Quittung?",
        yes: "Ja",
        no: "Nein",
        takeYourReceipt: "Bitte nehmen Sie Ihre Quittung",
        goBack: "Zurück",
    },
};

function changeLanguage(lang) {
    localStorage.setItem('language', lang);
    const elementsToTranslate = document.querySelectorAll('[data-translate]');
    elementsToTranslate.forEach(element => {
        const translationKey = element.dataset.translate;
        if (translations[lang] && translations[lang][translationKey]) {
            element.innerHTML = translations[lang][translationKey];
        }
    });
}

function loadStoredLanguage() {
    const storedLanguage = localStorage.getItem('language');
    if (storedLanguage) {
        changeLanguage(storedLanguage);
    } else {
        changeLanguage('en');
    }
}


// Load the stored language when the page is loaded
document.addEventListener('DOMContentLoaded', loadStoredLanguage);
