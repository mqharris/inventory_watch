"""
tests messanger
"""

import messanger


def test_send_text():
    """
    tests function
    """
    in_stock = {"name": "OnlineStatus", "value": "In Stock Online"}
    in_stock_code = 0
    out_of_stock = {"name": "OnlineStatus", "value": "Out of Stock Online"}
    out_of_stock_code = 1
    error1 = {"name": "asdf", "value": "Out of Stock Online"}
    error1_code = 2
    error2 = {"name": "OnlineStatus", "value": "asdf"}
    error2_code = 2

    #### TESTING FLAG IS TRUE
    message_text, recipients = messanger.send_text(in_stock,
                                                   in_stock_code,
                                                   testing_flag=True)
    assert message_text == "OnlineStatus : In Stock Online THIS IS ONLY A TEST"
    assert recipients == [messanger.mikes_number, messanger.mitchs_number]

    message_text, recipients = messanger.send_text(out_of_stock,
                                                   out_of_stock_code,
                                                   testing_flag=True)
    assert message_text == "OnlineStatus : Out of Stock Online THIS IS ONLY A TEST"
    assert recipients == []

    message_text, recipients = messanger.send_text(error1,
                                                   error1_code,
                                                   testing_flag=True)
    assert message_text == "asdf : Out of Stock Online Error in print code THIS IS ONLY A TEST"
    assert recipients == [messanger.mitchs_number]

    message_text, recipients = messanger.send_text(error2,
                                                   error2_code,
                                                   testing_flag=True)
    assert message_text == "OnlineStatus : asdf Error in print code THIS IS ONLY A TEST"
    assert recipients == [messanger.mitchs_number]
    #### TESTING FLAG IS TRUE

    #### TESTING FLAG IS FALSE
    message_text, recipients = messanger.send_text(
        out_of_stock,
        out_of_stock_code,
    )
    assert message_text == "OnlineStatus : Out of Stock Online"
    assert recipients == []

    message_text, recipients = messanger.send_text(
        error2,
        error2_code,
    )
    assert message_text == "OnlineStatus : asdf Error in print code"
    assert recipients == [messanger.mitchs_number]
    #### TESTING FLAG IS FALSE
