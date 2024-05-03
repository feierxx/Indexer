import psycopg2
import json

def msg_transfer(msg, conn, transac_id):

    #extract the required columns
    sender = msg['sender']
    receiver = msg['receiver']
    source_channel = msg['source_channel']
    denom = msg['token']['denom']
    amount = msg['token']['amount']
    
    #insertion to the table
    query = f"""
        INSERT INTO transc_transfer_msg (transac_id, sender, receiver, source_channel,denom,amount) 
        VALUES ('{transac_id}','{sender}','{receiver}','{source_channel}','{denom}','{amount}');
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


def msg_grant(msg, conn, transac_id):

    #extract the required columns
    granter = msg['granter']
    grantee = msg['grantee']
    authorization_type = msg['grant']['authorization']['@type']
    expiration = msg['grant']['expiration']
    
    try:
        allow_list = a['grant']['authorization']['msg']
    except KeyError:
        allow_list = None

    try:
        msg_i = msg['grant']['authorization']['msg']
    except KeyError:
        msg_i = None
    
    #insertion to the table
    query = f"""
        INSERT INTO transc_grant_msg (transac_id, granter, grantee, authorization_type,allow_list,msg,expiration) 
        VALUES ('{transac_id}','{granter}','{grantee}','{authorization_type}','{allow_list}','{msg_i}','{expiration}');
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


def msg_delegate(msg, conn, transac_id):

    #extract the required columns
    delegator_address = msg['delegator_address']
    validator_address = msg['validator_address']
    denom = msg['amount']['denom']
    amount = msg['amount']['amount']
    
    #insertion to the table
    query = f"""
        INSERT INTO transc_delegate_msg (transac_id, delegator_address, validator_address, denom, amount) 
        VALUES ('{transac_id}','{delegator_address}','{validator_address}','{denom}','{amount}');
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


def msg_revoke(msg, conn, transac_id):

    #extract the required columns
    granter = msg['granter']
    grantee = msg['grantee']
    msg_type_url = msg['msg_type_url']
    
    #insertion to the table
    query = f"""
        INSERT INTO transc_revoke_msg (transac_id, granter, grantee, msg_type_url) 
        VALUES ('{transac_id}','{granter}','{grantee}','{msg_type_url}');
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
        conn.rollback() 


def msg_beginredelegate(msg, conn, transac_id):

    #extract the required columns
    delegator_address = msg['delegator_address']
    validator_src_address = msg['grantee']
    validator_dst_address = msg['msg_type_url']
    denom = msg['amount']['denom']
    amount = msg['amount']['amount']

    #insertion to the table
    query = f"""
        INSERT INTO transc_beginredelegate_msg (transac_id, delegator_address, validator_src_address, validator_dst_address, denom, amount) 
        VALUES ('{transac_id}','{delegator_address}','{validator_src_address}','{validator_dst_address}','{denom}','{amount}');
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
        conn.rollback() 


def msg_withdraovalidatorcommission(msg, conn, transac_id):

    #extract the required columns
    validator_address = msg['validator_address']

    #insertion to the table
    query = f"""
        INSERT INTO transc_beginredelegate_msg (transac_id, validator_address) 
        VALUES ('{transac_id}','{validator_address}');
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
        conn.rollback() 