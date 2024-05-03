# Indexer Project
————EMRTS project

This project is designed to realize the ETL pipeline to extract proper information from the **blockchain data**, which is json format, transform it into proper type, and load it to the established **PostgreSQL relational datbase**.

## Instruction
### Prerequist:

Has postgreSQL environment downloaded. Required python packages, including requests, json, psycopg2 installed in the environment. A database for this indexer data should be firstly created.

### Scripts:

[file_loading.ipynb](file_loading.ipynb) is the main script from data fetching to data loading with the supporting functions from the .py documents. **_The .py documents should be downloaded to the same folder as the file_loading,ipynb._** The detailed explanation of the main script is as following:

**Step 1: Block Retrieving**

Specify the block number (block height) that is going to be loaded. The block_fetching function in [indexer_functions.py](indexer_functions.py) will enable the bloackchain json file loaded using API. 

Database connection will be established by calling the establish_db_connection function.

**Step 2: Block table insertion**

By calling block_insertion in [indexer_functions.py](indexer_functions.py), the main information about the file will be loaded to the _blocks_ table.

**Step 3: Transaction info decoding and insertion**

The transactions in the json file has been encoded. Calling the _decoding_ function in [indexer_functions.py](indexer_functions.py) and passing the transactions, it will return the decoded data. Fetch the corresponding generated block_id and insert the transactions info into _transactions_ table with [transaction_insertion](transaction_insertion).

**Step 4: Message Info insertion**

There are multiple message types. Therefore, there is a message_handler dictionary that automatically identify the meesage type and return the corresponding insertion function in [message_insertion.py](message_insertion.py). Each message in the file will be loaded to proper table with functions. _Currently the script only contains part of the message types._


### Testing

All the possible errors and exceptions are tried to be captured. Any unexpected outcome will be noticed by error message returning.

## ERD Diagram
![image](https://github.com/feierxx/Indexer/assets/158087978/62279192-4a57-47fd-b0ce-135da768e50e)


## Methodology
### Language

**Python:** Version 3.11.5


**PostgreSQL**: use PgAdmin 4 for interaction.
