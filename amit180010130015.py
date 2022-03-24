import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Root"
)

mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE mulesoft")
mycursor.execute("CREATE DATABASE mulesoft")
mycursor.execute("USE mulesoft")
mycursor.execute("CREATE TABLE movies(name VARCHAR(255), "
                 "actor VARCHAR(255), "
                 "actress VARCHAR(255), "
                 "director VARCHAR(255), "
                 "year INT(4))")
sql = "INSERT INTO movies(name, actor, actress, director, year) VALUES (%s , %s, %s, %s, %s)"
val = [
  ('ZINDAGI NA MILEGI DOBARA', 'HRITIK ROSHAN', 'KATRINA KAIF', 'ZOYA AKHTAR', 2011),
  ('DON ', 'SHAHRUKH KHAN ', 'PRIYANKA CHOPDA', 'FARHAN AKHTAR', 2006),
  ('BHAG MILKHA BHAG', 'FARHAN AKHTAR', 'SONAM KAPOOR', 'R O MEHRA', 2013),
  ('DEVDAS', 'SHAHRUKH KHAN', 'AISHVARYA RAI', 'SANJAY LEELA BHANSALI', 2002),
  ('MAIN HU NA', 'SHAHRUKH KHAN', 'SUSMITA SEN', 'FARA KHAN', 2004),
  ('RAMLEELA', 'RANVEER SINGH', 'DEEPIKA PADUKONE', 'SANJAY LEELA BHANSALI',2013)
]
mycursor.executemany(sql, val)

mycursor.execute("SELECT * FROM movies")

result = mycursor.fetchall()

for row in result:
    print(row)

print("")
mycursor.execute("SELECT * FROM movies WHERE actor = 'SHAHRUKH KHAN';")

result = mycursor.fetchall()

for row in result:
    print(row)
