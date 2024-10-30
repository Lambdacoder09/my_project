# my_functions.py

def get_connection(host="localhost", database="mydatabase", user="myuser", password="mypassword", port="5432"):
    """
    Establish a connection to the PostgreSQL database with customizable parameters.
    """
    import psycopg2
    
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        print("Connection to PostgreSQL established.")
        return connection
    except Exception as e:
        print("Error connecting to PostgreSQL:", e)
        return None
