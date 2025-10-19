import mysql.connector

try:
    db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "******"
    )

    mycursor = db.cursor()

# CREATE DATABASE 
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error:
    print("Not connected.")

finally:
    if db.is_connected():
        mycursor.close()
        db.close()