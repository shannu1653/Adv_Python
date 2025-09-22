import mysql.connector
from mysql.connector import Error

# your connection details
info = {
    'user': 'root',
    'password': 'Shanmukha@2002',
    'host': 'localhost',
    'port': 3308  # your MySQL port
}

db_name = "10000CODERS"
table_name = "53r batch"  # table name with space

conn = None
cursor = None

try:
    # 1) Connect to MySQL server
    conn = mysql.connector.connect(**info)
    cursor = conn.cursor()
    print("Connected to MySQL server")

    # 2) Create database and use it
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`;")
    cursor.execute(f"USE `{db_name}`;")
    print(f"Using database `{db_name}`")

    # 3) Create table
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS `{table_name}` (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        email VARCHAR(100),
        course VARCHAR(100)
    );
    """)
    print(f"Table `{table_name}` ready")

    # 4) Empty table before insert (so no duplicates on re-run)
    cursor.execute(f"TRUNCATE TABLE `{table_name}`;")

    # 5) Insert 5 records
    records = [
        ("shanmukh", 21, "shanmukh@example.com", "Python"),
        ("Naveen", 23, "Navven@example.com", "Web Dev"),
        ("Tharun", 22, "Tharun@example.com", "Data Science"),
        ("sathish", 24, "sathish@example.com", "React"),
        ("Akhil", 20, "Akhil@example.com", "Machine Learning")
    ]
    cursor.executemany(
        f"INSERT INTO `{table_name}` (name, age, email, course) VALUES (%s, %s, %s, %s)",
        records
    )
    conn.commit()
    print(f"Inserted {cursor.rowcount} records into `{table_name}`")


   # 6) Update shanmukh's email
    new_email = "shanmukh_new@example.com"
    cursor.execute(
        f"UPDATE `{table_name}` SET email = %s WHERE name = %s",
        (new_email, "shanmukh")
        
    )
    conn.commit()
    print("Updated shanmukh's email")


    # 6) Display data
    cursor.execute(f"SELECT * FROM `{table_name}`;")
    rows = cursor.fetchall()

    print("\nData in table:")
    print("-" * 70)
    print(f"{'ID':<3} {'Name':<10} {'Age':<3} {'Email':<25} {'Course'}")#space
    print("-" * 70)
    for r in rows:
        print(f"{r[0]:<3} {r[1]:<10} {r[2]:<3} {r[3]:<25} {r[4]}")
    print("-" * 70)

except Error as e:
    print("MySQL error:", e)

finally:

    
    if cursor is not None:
        cursor.close()
    if conn is not None and conn.is_connected():
        conn.close()
    print("Connection closed")
