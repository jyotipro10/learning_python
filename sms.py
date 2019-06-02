from twilio.rest import Client


account_sid = 'XXX' #my sid
auth_token = 'XXX'  #my auth token
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Avengers, Assemble!!!",
                     from_='+14064121939', #my temp no
                     to='+919800042266'
                 )

print(message.sid)
