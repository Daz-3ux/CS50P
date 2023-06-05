import sys
import requests

def main():
    cnt = get_cnt()
    price = float(get_price().replace(",", ""))
    money = cnt_to_price(cnt, price)
    print(f"${money:,.4f}")

def get_cnt():
    try:
        cnt = float(sys.argv[1])
        return cnt
    except ValueError:
        print("Command-line argument is not a number")
        exit(1)
    except IndexError:
        print("Missing command-line argument")
        exit(1)

def get_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        return o["bpi"]["USD"]["rate"]
    except requests.RequestException:
        pass

def cnt_to_price(cnt, price):
    return cnt * price


main()