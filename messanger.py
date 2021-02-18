"""
This module manages the functionality for sending sms's
"""

import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

ok_number = os.environ["OK_NUMBER"]
mikes_number = os.environ["MIKES_NUMBER"]
mitchs_number = os.environ["MITCHS_NUMBER"]


def send_text(status, print_code, testing_flag=False):
    """
    sends text message to hard coded number(s)
    """
    val = status["offers"]["6000202198563"]["gmAvailability"]
    message_text = ""
    recipients = []

    message_text = "{}".format(val)
    if print_code == 0:
        recipients = [mikes_number, mitchs_number]

    if print_code == 1:
        recipients = []

    if print_code == 2:
        message_text += " Error in print code"
        recipients = [mitchs_number]

    if testing_flag:
        message_text += " THIS IS ONLY A TEST"
        return message_text, recipients

    print("formatting text(s) to be sent if item is in stock")
    for number in recipients:
        message = client.messages \
                        .create(
                            body=message_text,
                            from_=ok_number,
                            to=number
                        )
        print(message.sid)
    return message_text, recipients


def error_sender(e):
    """
    send me a text if an error is encountered
    """
    message = client.messages \
                .create(
                    body="error : {}".format(e),
                    from_=ok_number,
                    to=mitchs_number
                )
    print(message.sid)
