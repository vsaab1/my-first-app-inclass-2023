from app.emailservice import send_email


def test_email_sending():
    
   assert send_email() == 202