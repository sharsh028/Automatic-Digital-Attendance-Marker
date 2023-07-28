import sqlite3

#establishing a connection with database
conn = sqlite3.connect('database/database.db')
c = conn.cursor()

#creating a table named students in database to record students credentials

c.execute("CREATE TABLE courses (course_id INTEGER PRIMARY KEY AUTOINCREMENT, course_name TEXT)")

c.execute("CREATE TABLE branch (branch_id INTEGER PRIMARY KEY AUTOINCREMENT, branch_name TEXT)")

c.execute("CREATE TABLE year (year_id INTEGER PRIMARY KEY AUTOINCREMENT, value TEXT)")

c.execute("CREATE TABLE students (Roll_number TEXT PRIMARY KEY, Name TEXT, course_id TEXT, branch_id TEXT, year_id TEXT, FOREIGN KEY(course_id) REFERENCES courses(course_id), FOREIGN KEY(branch_id) REFERENCES branch(branch_id), FOREIGN KEY(year_id) REFERENCES year(year_id))")

c.execute("INSERT INTO courses (course_name) VALUES ('B.Tech'), ('MBA'), ('Diploma')")
c.execute("INSERT INTO branch (branch_name) VALUES ('Computer Science'),('Electrical'),('Electronics'),('Mechanical'),('Civil'),('Agriculture')")
c.execute("INSERT INTO year (value) VALUES ('1st'),('2nd'),('3rd'),('4th'),('5th')")


#saving the changes in database
conn.commit()

#closing the connection
conn.close()