import sqlite3

conn = sqlite3.connect('babyorm.db')
c = conn.cursor()
c.execute("""CREATE TABLE `Users` (
		`id` INTEGER,
		`name` VARCHAR,
		`address` VARCHAR,
		`balance` REAL,
		PRIMARY KEY (`id`)
	)""")

c.execute("""CREATE TABLE `Stocks` (
		`id` INTEGER,
		`symbol` VARCHAR,
		`price` REAL,
		PRIMARY KEY (`id`)
	)""")
conn.commit()
conn.close()