import os

import requests
from dotenv import load_dotenv

load_dotenv()

MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_SENDER_ADDRESS = os.getenv("MAILGUN_SENDER_ADDRESS")
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN") # "sandbox__________.mailgun.org"

def send_email(recipient_address=MAILGUN_SENDER_ADDRESS, subject="[Shopping Cart App] Testing 123", html_content="<p>Hello World</p>"):
    print("SENDING EMAIL TO:", recipient_address)
    print("SUBJECT:", subject)
    print("HTML:", html_content)

    try:
        request_url = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages"
        message_data = {
            'from': MAILGUN_SENDER_ADDRESS,
            'to': recipient_address,
            'subject': subject,
            'html': html_content,
        }
        response = requests.post(request_url,
            auth=('api', MAILGUN_API_KEY),
            data=message_data
        )
        print("RESULT:", response.status_code)
        response.raise_for_status()
        print("Email sent successfully!")
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error sending email: {str(e)}")
        return None


if __name__ == '__main__':
    send_email()


