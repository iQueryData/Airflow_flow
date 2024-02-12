import psycopg2
import sys
import requests, json

import mysql.connector



try:
    conn = psycopg2.connect(host = "db",
                            port = "5432",
                          dbname = "dummyDB",
                          user = "postgres",
                          password = "postgres")  #host is the name in Docker-compose files & password
    
    cur = conn.cursor()

    insert_data = cur.execute("insert into dummy_schema.dummy (names) values ('docker');")

    cur.execute("select  * from dummy_schema.dummy;")
    rows = cur.fetchall()
    print(rows)


except Exception as err:
    print(f"Error Connecting to Postgres: {err}")



# Generate Data for ETL 

def gen_data():

    try:

        api_url = "https://randomuser.me/api/?results=10"

        response = requests.get(api_url).json()

        with open('sample.json', 'w') as api_data:
            api_data.write(json.dumps(response, indent=4))

        return True

    except Exception as err:

        print(f"Error During API Data Write : {err}")
        sys.exit(1)


# Do While Loop to connect to MySQL 
# Once the Connection is Successful, Insert Data froM Json File to MySQL
# How to Validate if a Connection Dropped during Insert and Data Lost ?
# Data Count Checks ? 

def mysql_connect():
    print("Inside MySQL connector")

    cnx = mysql.connector.connect(user='root', 
                                  password='root',
                                  host='localhost',
                                  port='3306',
                                  )
    
    cnx.execute("select  * from dummy_schema.dummy;")
    rows_mbd = cur.fetchall()
    print(rows_mbd)
    cnx.close()


mysql_connect()