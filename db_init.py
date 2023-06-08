import sqlite3

# Step 1: Establish a connection to the SQLite database
conn = sqlite3.connect('pets.db')

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Read and execute the SQL script file
script_file = 'db_init.sql'
with open(script_file, 'r') as f:
    sql_script = f.read()

cursor.executescript(sql_script)

# Step 4: Commit the changes
conn.commit()

# Step 5: Close the cursor and the connection
cursor.close()
conn.close()
