import pandas as pd


from my_func import*

def main():
    conn = get_connection(
        host="localhost",
        database="mydatabase",
        user="myuser",
        password="mypassword",
        port="5432"
    )
    
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        print(cursor.fetchone())
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
