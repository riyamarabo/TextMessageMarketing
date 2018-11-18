import pandas as pd

df = pd.read_csv('customers.csv', usecols=['mobile']).values.tolist()

phones = []

for number in df:
    phones.append(number)

# import nexmo
#
# client = nexmo.Client(key='null', secret='null')

# for numbers in phones:
#
#     client.send_message({
#         'from': '18665207093',
#         'to': numbers,
#         'text': "testing number upload from csv",
#     })



import plivo

client = plivo.RestClient('null', 'null')

for numbers in phones:
    try:
        response = client.messages.create(
            src='18553653838',
            dst=numbers[0],
            text="Your blast message here",
        )
    except plivo.exceptions.PlivoRestError as e:
        print(e)
