"""
tests searcher
"""
import searcher

out_of_stock_mock = {
    'skus': {
        '6000202198563': ['6000202198563']
    },
    'offers': {
        '6000202198563': {
            'gmAvailability': 'OutOfStock',
            'priceCompUomCd': 'EA',
            'limitedQuantity': True,
            'priceCompQty': 1,
            'save': False,
            'autoSave': False,
            'offerRank': 1,
            'pricePerUnit': 629.96,
            'offerType': '1P',
            'offerSchedulable': False,
            'sellerId': '0',
            'clearance': False,
            'availableQuantity': 0,
            'priceScheduled': False,
            'currentPrice': 629.96,
            'reduced': False,
            'preOrderFlag': False,
            'hidePrice': False,
            'taxCode': '2042447',
            'sellerInfo': {
                'en': 'Walmart',
                'fr': 'Walmart'
            },
            'badges': [],
            'rollBack': False,
            'minAdvPrice': 0,
            'offerId': '6000202198563',
            'groceryAvailability': 'NotSold'
        }
    },
    'priceZone': {
        '6000202198562': '2022'
    },
    'sellerDetails': {}
}

in_stock_mock = {
    "skus": {
        "6000198805449": ["6000198805449"]
    },
    "offers": {
        "6000202198563": {
            "gmAvailability": "Available",
            "priceCompUomCd": "EA",
            "limitedQuantity": False,
            "priceCompQty": 1,
            "save": False,
            "autoSave": False,
            "offerRank": 1,
            "pricePerUnit": 379.96,
            "offerType": "1P",
            "offerSchedulable": False,
            "sellerId": "0",
            "clearance": False,
            "availableQuantity": 252,
            "priceScheduled": False,
            "currentPrice": 379.96,
            "reduced": False,
            "preOrderFlag": False,
            "hidePrice": False,
            "taxCode": "2042447",
            "sellerInfo": {
                "en": "Walmart",
                "fr": "Walmart"
            },
            "badges": [],
            "rollBack": False,
            "minAdvPrice": 0,
            "offerId": "6000198805449",
            "groceryAvailability": "NotSold"
        }
    },
    "priceZone": {
        "6000199709949": "2022"
    },
    "sellerDetails": {}
}


def test_stock_status():
    """
    tests function with saved data
    """
    check_code = searcher.check_stock_status(out_of_stock_mock)
    assert check_code == 1
    check_code = searcher.check_stock_status(in_stock_mock)
    assert check_code == 0
