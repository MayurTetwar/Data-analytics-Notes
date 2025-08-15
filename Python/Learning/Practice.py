
import psycopg2

conn =psycopg2.connect(
    host='localhost',
    dbname='bankdb',
    user='postgres',
    password='root',
    post_id=5432
)

conn.close()