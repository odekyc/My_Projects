import sqlite3
import csv


class Database:
	def __init__(self, dbfile):
		self.mydb=dbfile+".db"
		self.con=None
		self.curs=None

	def connect(self):
		self.con=sqlite3.connect(self.mydb)

	def cursor(self):
		self.curs=self.con.cursor()

	def commit(self):
		self.con.commit()

	def close_connection(self):
		self.con.close()


class CSV:
	def __init__(self, csvfile):
		self.mycsvfile=csvfile+".csv"
		self.file=None
		self.myfieldnames=('Username','Password')
		self.reader=None
		self.writer=None
	def openreader(self):
		self.file=open(self.mycsvfile, 'rt')

	def openwriter(self):
		self.file=open(self.mycsvfile, 'a')

	def dictreader(self):
		self.reader=csv.DictReader(self.file)
	

	def dictwriter(self):
		self.writer=csv.DictWriter(self.file,fieldnames=self.myfieldnames )


	def close(self):
		self.file.close()
