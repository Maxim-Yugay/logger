import psycopg2


conn = psycopg2.connect(
    host='localhost',
    port=5432,
    dbname='postgres',
    user='postgres',
    password=12345,
    sslmode='prefer',
    connect_timeout=10,
)
cur = conn.cursor()

cur.execute(
    "CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);"
)

cur.execute(
    "INSERT INTO test (num, data) VALUES (%s, %s)",
    (100, "abc'def")
)


cur.execute("SELECT * FROM test;")

cur.fetchone()
conn.commit()

cur.close()
conn.close()