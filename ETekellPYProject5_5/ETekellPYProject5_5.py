import sqlite3 as sl

#create and connect to db my-test.db
con = sl.connect('my-test.db')

#create cursor object
c = con.cursor()

#execute command on db
#execute command on db
c.execute('''SELECT count(name) FROM sqlite_master WHERE type ='table' AND name ='Movies' ''')

if c.fetchone()[0]==1:
	print('Table exists')
else:
	print('Table does not exist')
	#create table
	with con:
		con.execute("""
			CREATE TABLE Movies (
				MovieId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
				MovieName TEXT,
				Genre TEXT,
				ReleaseDate INTEGER
			);
			""")
	#create sql to insert 
	sql = "INSERT INTO Movies (MovieID, MovieName, Genre, ReleaseDate) values (?,?,?,?)"
	data = [
		(1, 'Raiders of the Lost Ark', 'Action-Adventure', 1981),
		(2, 'Indiana Jones and The Temple of Doom', 'Action-Adventure', 1984),
		(3, 'Indiana Jones and The Kingdom of the Crystal Skull', 'Action-Adventure', 2008),
		(4, 'Indiana Jones and The Last Crusade', 'Action-Adventure', 1989),
		(5, 'The Departed', 'Drama', 2006),
		(6, 'Shutter Island', 'Drama', 2010),
		(7, 'First Blood', 'Action', 1982),
		(8, 'Rambo:First Blood Part Two', 'Action', 1985),
		(9, 'Rambo III', 'Action', 1988),
		(10, 'Rambo', 'Action', 2008)
	]
	#run query
	with con:
		con.executemany(sql, data)
#connect and read data
print("First Query******************")
with con:
	data = con.execute("SELECT * FROM Movies WHERE ReleaseDate >= 2000;")
	for row in data:
		print(row)

print("\nSecond Query******************")
with con:
	data = con.execute("SELECT * FROM Movies WHERE ReleaseDate < 2000;")
	for row in data:
		print(row)

