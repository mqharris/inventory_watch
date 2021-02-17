"""
scrapes walmart's website to see if item-x is in stock
"""

# from bs4 import BeautifulSoup
# import requests

# def scrape_page():
#     """
#     Scrapes the webpage to see if the item is available online
#     """
#     page = requests.get(
#         "https://www.bestbuy.ca/en-ca/product/playstation-5-console-online-only/14962185"
#     )
#     soup = BeautifulSoup(page.content, 'html.parser')
#     print(soup)
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_response_from_site():
    """
    loads site and gets response as a string
    """
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(
        "https://www.walmart.ca/en/ip/playstation5-console/6000202198562")

    response = driver.page_source

    driver.quit()

    return response


def parse_resp_for_stock_status(res):
    """
    searches resp for the substring saying if item is in stock
    """
    idx = res.find('"id":23,"name":"OnlineStatus"')
    left_trim = res[idx - 1:]
    right_trim = left_trim[:left_trim.find("}") + 1]
    status = json.loads(right_trim)
    return status


def check_stock_status(stock_status):
    """
    checks the scrapped data if the item is in stock
    """
    status = stock_status["value"]
    status_name = stock_status["name"]
    if (status_name == "OnlineStatus") and (status == "In Stock Online"):
        print("Item in stock")
    elif (status_name == "OnlineStatus") and (status == "Out of Stock Online"):
        print("Item not in stock")
        return 1
    else:
        print("error with checking stock status")
        return 2
    return 0


if __name__ == "__main__":
    resp = open("test_resp.txt", "r").read()
    parse_resp_for_stock_status(resp)
