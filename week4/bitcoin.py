import os
import sys
import requests


def main():
    if len(sys.argv) != 2:                 # program name + how many arguments?
        sys.exit("Missing command-line argument")

    try:
        # which index holds the user's number?
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=dd5c0864b5aeac62b585c5d518791e95d740da4ca4d1fb93eabe25e690563c86"
        )

        data = response.json()
        # which key holds the USD price?
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Request failed")

    print(f"${price * n:,.4f}")


main()
