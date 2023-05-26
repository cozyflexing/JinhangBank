input = 900
options = {
    "50": [{"value": 50}, {"amount": 6}],
    "20": [{"value": 20}, {"amount": 6}],
    "10": [{"value": 10}, {"amount": 6}],
}
bills = []

if input % 10 != 0:
    print("Invalid input. Please enter an amount that is a multiple of 10.")
else:
    while input != 0:
        if input > 480:
            print("Please take a lesser amount")
            break
        else:
            if input >= options["50"][0]["value"] and options["50"][1]["amount"] > 0:
                input -= options["50"][0]["value"]
                bills.append(options["50"][0]["value"])
                options["50"][1]["amount"] -= 1
            elif input >= options["20"][0]["value"] and options["20"][1]["amount"] > 0:
                input -= options["20"][0]["value"]
                bills.append(options["20"][0]["value"])
                options["20"][1]["amount"] -= 1
            elif input >= options["10"][0]["value"] and options["10"][1]["amount"] > 0:
                input -= options["10"][0]["value"]
                bills.append(options["10"][0]["value"])
                options["10"][1]["amount"] -= 1
            else:
                print("Not enough bills for requested amount.")
                break
    print(f"Dispensed bills: {bills}")
