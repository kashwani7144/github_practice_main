import cx_Oracle

# Set up the connection details
username = 'ASHWANI'
password = 'toor'
dsn = 'orcl'  # Data Source Name (TNS entry or Easy Connect)

try:
    # Establish a connection to the Oracle database
    session = cx_Oracle.connect(username, password, dsn)
    print(f"!!! Oracle Database Connection Successful !!!")

    # Create a cursor
    cursor = session.cursor()
    print(f"cursor variable 'cursor' created.")

except cx_Oracle.Error as error:
    print("Error occurred:", error)
