import psycopg2
import sys
import requests, json


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


# def insert_to_db():
#     if gen_data():
#         # Do Database Connection 
#         while time_out < 10:
#             time_out = 0 
#             time_out += 1

#             conn = psycopg2.connect('HOST',
#                                     'PORT',
#                                     'DATABASE',
#                                     'USERNAME',
#                                     'PASSWORD')
            