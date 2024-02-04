import psycopg2


try:
    conn = psycopg2.connect(host = "localhost",
                            port = "5432",
                          database = "dummyDB",
                          user = "postgres",
                          password = "postgres")
    
    cur = conn.cursor()

    insert_data = cur.execute("insert into dummy_schema.dummy (names) values ('docker');")

    cur.execute("select  * from dummy_schema.dummy;")
    rows = cur.fetchall()
    print(rows)


except Exception as err:
    print(f"Error Connecting to Postgres: {err}")
