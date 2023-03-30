import mysql.connector

# Establish a connection to the database
cnx = mysql.connector.connect(
    user="ubuntu-1051158",
    password="NS24^vpY",
    host="145.24.222.16",
    database="JinhangBank",
)

# Create a cursor object
cursor = cnx.cursor()

# Execute a query
query = "SELECT * FROM klanten"
cursor.execute(query)

# Fetch the results
result = cursor.fetchall()

# Print the results
for row in result:
    print(row)

# Close the cursor and connection
cursor.close()
cnx.close()
