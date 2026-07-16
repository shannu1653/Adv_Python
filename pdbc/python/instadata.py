import mysql.connector
conn=mysql.connector.connect(
user='root',
password='Shanmukha@2002',
host='localhost',
port=3308
)
print("connect")
cursor=conn.cursor()

# #1.create database
# try:
#     query="""create database if not exists instadata """
#     cursor.execute(query)
#     print('database created succesfully')
# except:
#     print('database not created')

# ##2.use database
# try:
#     query="""use instadata"""
#     cursor.execute(query)
#     print('now data in database')
# except:
#     print('error occured')


# # #3.create table
# try:
#     create_table = """
#     CREATE TABLE IF NOT EXISTS data (
#         userno INT AUTO_INCREMENT PRIMARY KEY,
#         userid INT UNIQUE,
#         username VARCHAR(100),
#         password VARCHAR(100),
#         likes BIGINT,
#         followers BIGINT,
#         comments BIGINT
#     )
#     """
#     cursor.execute(create_table)
#     print("Table successfully created")
# except Exception as e:
#     print("Table not created:", e)


# query="""alter table data add  views bigint"""
# cursor.execute(query)


# #4.# insert multiple rows at a time
# def insertMulRow(data):
#     try:
#         insertdata = """
#         INSERT INTO data (userid, username, password, likes, followers, comments)
#         VALUES (%s, %s, %s, %s, %s, %s)
#         """
#         cursor.executemany(insertdata, data)
#         print("Data inserted successfully for multiple rows")
#     except Exception as e:
#         print('Error inserting multiple rows:', e)

# # Correct number of values (6 for each row)
# insertMulRow([
#     (124, 'navven', 'naveen123', 200, 3400, 2000),
#     (126, 'tharun', 'tharun123', 2020, 3800, 2030),
#     (127, 'sathish', 'sathish123', 2900, 3500, 2020),
#     (128, 'akhil', 'akhil123', 200, 3060, 2400),
#     (129, 'sharanya', 'sharanya123', 2300, 3080, 2400),
#     (130, 'aneela', 'aneela123', 2030, 3300, 2030),
#     (131, 'suppu', 'suppu123', 203, 3030, 2700)
# ])


# query="""alter table data add  views int"""
# cursor.execute(query)

# query="""update data set views=1000 where userno=2"""
# cursor.execute(query)





conn.commit()
cursor.close()
conn.close()