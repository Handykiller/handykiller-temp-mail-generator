from mailtm import Email

def listener(message):
    print("\nSubject: " + message['subject'])
    print("Content: " + (message['text'] if message['text'] else message['html']))

test = Email()
print("\nDomain: " + test.domain)

test.register()
print("\nEmail Address: " + str(test.address))

test.start(listener)
print("\nWaiting for new emails...")
