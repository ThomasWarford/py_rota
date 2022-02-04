# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 13:51:25 2022

@author: Thoma
"""
import pandas as pd
from twilio.rest import Client

ACCOUNT_SID = 'x'
AUTH_TOKEN = 'x'
TWILIO_NUMBER = 'x'
FILE_NAME = 'users.csv'


def retrieve_entry(file_name: str) -> list:
    '''
    Returns top row of csv and moves entry to the bottom of csv.

    Parameters
    ----------
    file_name : str

    Returns
    -------
    top_entry : list

    '''
    user_data = pd.read_csv(file_name, header=None, delimiter=',',
                            dtype={1: str})
    user_data = user_data.transpose()
    top_entry = user_data.pop(0)

    user_data = user_data.transpose()
    user_data = user_data.append(top_entry)
    user_data.to_csv(file_name, index=False, header=False)
    return top_entry

def main():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    unlucky = retrieve_entry(FILE_NAME)


    message = client.messages.create(
        to=unlucky[1],
        from_=TWILIO_NUMBER,
        body=f'It\'s your turn to empty the bins, {unlucky[0]}. Unlucky!')
    with open('log.csv', 'a') as log_file:
        print(message.sid, file=log_file)

if __name__ == '__main__':
    main()


