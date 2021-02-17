"""
tests searcher
"""
import searcher


def test_parse_resp_for_in_stock():
    """
    tests function with saved data
    """
    resp = open("test_resp.txt", "r").read()
    status = searcher.parse_resp_for_stock_status(resp)
    assert status["name"] == "OnlineStatus"
    assert status["value"] == "Out of Stock Online"


def test_stock_status():
    """
    tests function with saved data
    """
    resp = open("test_resp.txt", "r").read()
    out_of_stock = searcher.parse_resp_for_stock_status(resp)
    check_code = searcher.check_stock_status(out_of_stock)
    assert check_code == 1
    in_stock = {"name": "OnlineStatus", "value": "In Stock Online"}
    check_code = searcher.check_stock_status(in_stock)
    print(check_code)
    assert check_code == 0
    should_error = {"name": "asdf", "value": "Out of Stock Online"}
    check_code = searcher.check_stock_status(should_error)
    assert check_code == 2
    should_error = {"name": "OnlineStatus", "value": "asdfsfasf"}
    check_code = searcher.check_stock_status(should_error)
    assert check_code == 2
