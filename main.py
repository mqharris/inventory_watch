"""
This module puts everything together and is the entry point
"""
import time

import searcher
import messanger

if __name__ == "__main__":
    while True:
        try:
            resp = searcher.get_response_from_site()
            print_code = searcher.check_stock_status(resp)
            message_text, recipients = messanger.send_text(resp, print_code)
            print(message_text, recipients)
        except Exception as error:
            messanger.error_sender(error)
        if print_code == 0:
            break
        time.sleep(300)
