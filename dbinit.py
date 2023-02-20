import sqlite3, random


names = ["Clifton","Ryann","Kashmir","Garren","Cole","Cheston","Keisy","Breanna","Lucius","Eris"]
passwords = ["timetable345", "reckless82354", "humour7287", "flush5329", "soprano5", "gravity63", "competence42", "foster512", "elect333", "ivory534"]
data = []
for i in range(0,9):
    data.append([names[i], passwords[i], random.choice(['Active', 'Inactive'])])
print(data)

with con as sqlite3.connect("users.db"):
    cur = con.cursor()
    cur.execute("CREATE TABLE users(name, password, active)")
    cur.executemany("INSERT INTO users VALUES(?, ?, ?)", data)
    con.commit()