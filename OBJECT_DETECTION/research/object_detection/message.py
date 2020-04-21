from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

def send_alert(content):
    account_sid = 'AC56cdc5129a5b8bbfa5098d4e5f6c3086'
    auth_token = 'bcee0cc2a1e742c44db2e4e002c720c9'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=content,
                         from_='+19382383136',
                         to='+919381766403'
                     )

    print(message.sid)

send_alert("crap")
