import psycopg2
import requests

def block_fetching(block_id):
    # Make the API request
    url = f"http://116.202.143.93:1317/cosmos/base/tendermint/v1beta1/blocks/{block_id}"
    response = requests.get(url)
    file = response.json() #report as json file
    return file

def establish_db_connection():
    dbname = 'transaction'
    username = 'feierx'
    password = 'rootroot'
    host = 'localhost'
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(dbname=dbname, user=username, password=password, host=host)
        print("Connection successful!")
        return conn

    except psycopg2.Error as e:
        print("Error connecting to the database:")
        print(e)
        return None

def decoding(txs):
    payload = {
        "tx_bytes": txs  # Make sure this is the transaction data as a string
    }


    url = 'https://phoenix-lcd.terra.dev/cosmos/tx/v1beta1/decode'

    # The headers, including the content type
    headers = {
        "Content-Type": "application/json",
    }

    # Sending the POST request to the API with the correctly formatted payload
    response = requests.post(url, headers=headers, json=payload)

    # Checking if the request was successful
    if response.status_code == 200:
        # Decoding the response data
        decoded_data = response.json()  # This will be a dictionary
        print("Sucessfully decoded!")
    else:
        print("Failed to decode data:", response.status_code, response.text)
    return decoded_data


