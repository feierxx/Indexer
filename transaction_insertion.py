import psycopg2
import json

def transaction_insertion(decoded_file, conn, block_id):

    #extract the required columns
    memo = decoded_file['tx']['body']['memo']
    fee_denom = decoded_file['tx']['auth_info']['fee']['amount'][0]['denom']
    fee_amount = decoded_file['tx']['auth_info']['fee']['amount'][0]['amount']
    gas_limit = decoded_file['tx']['auth_info']['fee']['gas_limit']
    tx = json.dumps(decoded_file)
    #insertion to the table
    query = f"""
        INSERT INTO transactions (block_id, transc_type_id, memo, fee_denom,fee_amount,gas_limit,tx) 
        VALUES ('{block_id}','{memo}','{fee_denom}','{fee_amount}','{gas_limit}','{tx}')
        RETURNING transac_id;
    """
    try:
        cur = conn.cursor()
        cur.execute(query)
        transac_id = cur.fetchone()[0]    
        conn.commit()
        print("Transaction committed successfully.Transaction ID:", transac_id)
        return transac_id
    
    except psycopg2.Error as e:
        # Catch any database errors during the commit
        print("Error committing transaction:")
        print(e)
        conn.rollback()  # Rollback the transaction on error
    except Exception as e:
        # Catch any other exceptions
        print("An unexpected error occurred during the transaction:")
        print(e)
        conn.rollback()  # Rollback the transaction on error
