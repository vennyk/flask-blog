import sqlite3

with sqlite3.connect("blog.db") as conn:
	c = conn.cursor()
	c.execute("""CREATE TABLE posts (title TEXT, post TEXT)""")

	c.execute('INSERT INTO posts VALUES("Good", "I am good")')
	c.execute('INSERT INTO posts VALUES("Well", "I am well")')
	c.execute('INSERT INTO posts VALUES("Fine", "I am fine")')
	c.execute('INSERT INTO posts VALUES("Ok", "I am ok")')