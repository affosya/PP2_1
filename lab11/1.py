import psycopg2

# Establishing connection to PostgreSQL database
conn = psycopg2.connect(
    dbname="your_db_name", 
    user="your_db_user", 
    password="your_db_password", 
    host="localhost", 
    port="5432"
)

# Creating a cursor object using the connection
cur = conn.cursor()

# Function to call a stored procedure to insert or update user
def insert_or_update_user(name, phone):
    cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
    conn.commit()

# Function to query records by pattern
def get_records_by_pattern(pattern):
    cur.execute("SELECT * FROM get_records_by_pattern(%s);", (pattern,))
    records = cur.fetchall()
    for record in records:
        print(record)

# Function to query data with pagination
def query_data_with_pagination(limit, offset):
    cur.execute("SELECT * FROM query_data_with_pagination(%s, %s);", (limit, offset))
    records = cur.fetchall()
    for record in records:
        print(record)

# Function to delete a user by name or phone
def delete_user(identifier):
    cur.execute("CALL delete_user_by_identifier(%s);", (identifier,))
    conn.commit()

# Example usage
insert_or_update_user("John Doe", "1234567890")
get_records_by_pattern("John")
query_data_with_pagination(10, 0)
delete_user("John Doe")

# Close the cursor and connection
cur.close()
conn.close()
