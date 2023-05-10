import mysql.connector

# Establish a connection to the MariaDB database
connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Alenheefteenmacminiuit2022",  # Replace with your own password
    database="JinhangBank",
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Define the SQL query
sql_query = "SELECT * FROM klanten;"

# Execute the SQL query using the cursor
cursor.execute(sql_query)

# Fetch all rows from the executed query
rows = cursor.fetchall()

# Print the fetched rows
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
