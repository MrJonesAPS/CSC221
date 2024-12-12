# Run these terminal commands first to create this db
"""
sqlite3 my.db
SQLite version 3.43.2 2023-10-10 13:08:14
Enter ".help" for usage hints.
sqlite> create table appointments(start datetime,length_mins integer);
sqlite> insert into appointments(start,length_mins)values('2024-12-12',60),('2024-12-13',60);
sqlite> select * from appointments;
2024-12-12|60
2024-12-13|60
"""

# sqlite starter code from: https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
import sqlite3


# Define our "template" HTML code
html_top = """
<!DOCTYPE html>
<html lang='en'>
<head>
    <title>Jeff's Appointments</title>
</head>
<body>
<table>
<tr>
<th>Date</th><th>Time (Minutes)</th>
</tr>
"""

html_bottom = """
</table>
</body>
</head>
"""

html_mid = ""

# Connect to the db and query the data
try:
    with sqlite3.connect("my.db") as conn:
        cur = conn.cursor()
        cur.execute("select start, length_mins from appointments")
        rows = cur.fetchall()
        # for each record in the table, create one new HTML table row
        for row in rows:
            html_mid += f"<tr><td>{row[0]}</td><td>{row[1]}</td></tr>"
except sqlite3.OperationalError as e:
    print(e)

# Write it all out to a file
with open("out.html", "w") as out:
    out.write(html_top)
    out.write(html_mid)
    out.write(html_bottom)
