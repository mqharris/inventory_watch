"""
This module puts everything together and is the entry point
"""

import searcher
import messanger

if __name__ == "__main__":
    try:
        resp = searcher.get_response_from_site()
        print_code = searcher.check_stock_status(resp)
        message_text, recipients = messanger.send_text(resp, print_code)
        print(message_text, recipients)
    except Exception as error:
        messanger.error_sender(error)
