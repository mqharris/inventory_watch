"""
This module puts everything together and is the entry point
"""

import searcher
import messanger

if __name__ == "__main__":
    resp = searcher.get_response_from_site()
    status = searcher.parse_resp_for_stock_status(resp)
    print_code = searcher.check_stock_status(status)
    message_text, recipients = messanger.send_text(status, print_code)
    print(message_text, recipients)
