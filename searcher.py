"""
scrapes walmart's website to see if item-x is in stock
"""

import json
import requests


def get_response_from_site():
    """
    loads site and gets response as a string
    """
    headers = {
        'authority': 'www.walmart.ca',
        'accept': 'application/json',
        'content-type': 'application/json',
        'user-agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'wm_qos.correlation_id':
        '04db18a4-026-177b19643694ce,04db18a4-026-177b196436940b,04db18a4-026-177b196436940b',
        'origin': 'https://www.walmart.ca',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer':
        'https://www.walmart.ca/en/ip/playstation5-console/6000202198562',
        'accept-language': 'en-US,en;q=0.9',
    }

    data = '{"fsa":"L5V","products":[{"productId":"6000202198562","skuIds":["6000202198563"]}],"lang":"en","pricingStoreId":"1061","fulfillmentStoreId":"1061","experience":"whiteGM"}'

    response = requests.post(
        'https://www.walmart.ca/api/product-page/v2/price-offer',
        headers=headers,
        data=data)

    resp_json = response.content.decode('utf8').replace("'", '"')
    data = json.loads(resp_json)
    return data


def check_stock_status(site_json):
    """
    checks the scrapped data if the item is in stock
    """
    status = site_json["offers"]["6000202198563"]["gmAvailability"]
    print(status)
    if status == "Available":
        print("Item in stock")
    elif status == "OutOfStock":
        print("Item not in stock")
        return 1
    else:
        print("error with checking stock status")
        return 2
    return 0


if __name__ == "__main__":
    resp = get_response_from_site()
    print(resp)
    stuff = resp["offers"]["6000202198563"]["gmAvailability"]
    print(stuff)
