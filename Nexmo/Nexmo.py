"""
To do:
1. Corner case: must be 10 numbers and start with 1, if nine, add one, if n < 9 reject
2. Schedule cron job
3. place names of blasts in a sheet to read with message to blast
4. read report/log
"""

import nexmo
import plivo
import pandas as pd

# def collectNumbers():
#     """Collecting numbers from specific excel sheet"""



#     return phones
#
# # def nexmoService(phones):
#     """Function to activate Nexmo Service"""
#
#     client = nexmo.Client(key='null', secret='null')
#
#     for numbers in phones:
#
#         client.send_message({
#             'from': '18665207093',
#             'to': numbers,
#             'text': "testing number upload from csv",
#         })



# def plivoService(phones):
#     """Function to activate Plivo Service"""

client = plivo.RestClient('null', 'null')

phones = []

df = pd.read_csv('shoppers.csv', usecols=['Mobile']).values.tolist()

for number in df:
    phones.append(int(number[0]))

print(phones)


for numbers in phones:
    try:
        response = client.messages.create(
            src='18553653838',
            dst=numbers,
            text="Thanksgiving specials at Shoppers Market on 22800 Van Dyke, Warren. See specials here https://goo.gl/37XZa9 Reply STOP to quit.",
        )
        print("\nmsg delivered to: " , str(numbers))
    except plivo.exceptions.PlivoRestError as e:
        print(e)

# def main():
#     print(collectNumbers())
#
# if __name__ == '__main__':
#     main()
