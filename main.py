"""
This module puts everything together and is the entry point
"""

import searcher
import messanger

if __name__ == "__main__":
    resp = searcher.get_response_from_site()
    print(resp)
    print_code = searcher.check_stock_status(resp)
    print(print_code)
    message_text, recipients = messanger.send_text(resp, print_code)
    print(message_text, recipients)
