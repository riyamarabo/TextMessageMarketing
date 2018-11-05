import nexmo

client = nexmo.Client(key='null', secret='null')

phones = [16197295998, 16198887517]

for numbers in phones:
    for trials in range(1, 101):
        text = "test: " + str(trials)

        client.send_message({
            'from': '18665207093',
            'to': numbers,
            'text': text,
        })
        print(numbers, ": ", text)



import plivo

phones = [16197295998, 16198887517]

client = plivo.RestClient('null', 'null')

for numbers in phones:
    for trials in range(1, 101):
        text = "test: " + str(trials)
        try:
            response = client.messages.create(
                src='18553653838',
                dst=numbers,
                text=text,
            )
            print(numbers, ": ", text)
        except plivo.exceptions.PlivoRestError as e:
            print("exception printed")
