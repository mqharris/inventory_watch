"""
tests messanger
"""

import messanger

out_of_stock_mock = {
    'skus': {
        '6000202198563': ['6000202198563']
    },
    'offers': {
        '6000202198563': {
            'gmAvailability': 'OutOfStock',
            'priceCompUomCd': 'EA',
            'limitedQuantity': True,
        }
    }
}

in_stock_mock = {
    'skus': {
        '6000202198563': ['6000202198563']
    },
    'offers': {
        '6000202198563': {
            'gmAvailability': 'Available',
            'priceCompUomCd': 'EA',
            'limitedQuantity': True,
        }
    }
}


def test_send_text():
    """
    tests function
    """
    in_stock_code = 0
    out_of_stock_code = 1

    #### TESTING FLAG IS TRUE
    message_text, recipients = messanger.send_text(in_stock_mock,
                                                   in_stock_code,
                                                   testing_flag=True)
    assert message_text == "Available THIS IS ONLY A TEST"
    assert recipients == [messanger.mitchs_number]

    message_text, recipients = messanger.send_text(out_of_stock_mock,
                                                   out_of_stock_code,
                                                   testing_flag=True)
    assert message_text == "OutOfStock THIS IS ONLY A TEST"
    assert recipients == []
    #### TESTING FLAG IS TRUE

    #### TESTING FLAG IS FALSE
    message_text, recipients = messanger.send_text(
        out_of_stock_mock,
        out_of_stock_code,
    )
    assert message_text == "OutOfStock"
    assert recipients == []
    #### TESTING FLAG IS FALSE
