def main():
    cents = get_cents()

    quarter = 0.25
    quarters = calculate_currency_to_hand(quarter, cents)
    cents = round(cents - quarters * quarter, 2)

    dime = 0.1
    dimes = calculate_currency_to_hand(dime, cents)
    cents = round(cents - dimes * dime, 2)

    nickel = 0.05
    nickels = calculate_currency_to_hand(nickel, cents)
    cents = round(cents - nickels * nickel, 2)

    penny = 0.01
    pennies = calculate_currency_to_hand(penny, cents)
    cents = round(cents - pennies * penny, 2)

    coins = quarters + dimes + nickels + pennies

    print(coins)


def get_cents():
    while True:
        try:
            cents = float(input("Change owed: "))
            if cents > 0.0:
                return cents
        except ValueError:
            pass


def calculate_currency_to_hand(unit, cents):
    currency_to_hand = 0
    while cents >= unit:
        currency_to_hand += 1
        cents -= unit
    return currency_to_hand


if __name__ == "__main__":
    main()
