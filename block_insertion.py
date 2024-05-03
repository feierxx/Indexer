
import psycopg2

def block_insertion(file,conn):

    #extract the required columns
    chain_id = file['block']['header']['chain_id']
    height = file['block']['header']['height']
    create_time = file['block']['header']['time']
    block_hash = file['block_id']['hash']

    #insertion to the table
    query = f"""
        INSERT INTO blocks (block_hash, chain_id, height, create_time) 
        VALUES ('{block_hash}','{chain_id}','{height}','{create_time}');
    """
    try:
        cur = conn.cursor()
        cur.execute(query)     
        conn.commit()
        print("Transaction committed successfully.")
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


