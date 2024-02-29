import csv
import sqlite3
from faker import Faker
from datetime import datetime
from faker.providers import address, internet, person

#opening connection to the database/ creates database if not found
conn = sqlite3.connect("database.db")
cur = conn.cursor()
fake = Faker()

conn.execute("DROP TABLE IF EXISTS e_address_details")
conn.execute("DROP TABLE IF EXISTS e_company_details")
conn.execute("DROP TABLE IF EXISTS e_contact_details")
conn.execute("DROP TABLE IF EXISTS e_personal_details")
print("table dropped successfully")

conn.execute("CREATE TABLE e_personal_details (id INTEGER PRIMARY KEY AUTOINCREMENT, f_name TEXT, l_name TEXT, gender TEXT, b_date DATE, age INTEGER, name_pre TEXT)")
conn.execute("CREATE TABLE e_contact_details (id INTEGER PRIMARY KEY AUTOINCREMENT, phone_no INTEGER, email TEXT, emergency_phone INTEGER, emp_id INTEGER, FOREIGN KEY(emp_id) REFERENCES e_personal_details(id) )")
conn.execute("CREATE TABLE e_company_details (id INTEGER PRIMARY KEY AUTOINCREMENT, DOJ DATE, MOJ TEXT, age_in_company INTEGER, salary INTEGER, emp_id INTEGER, emp_email TEXT, FOREIGN KEY(emp_id) REFERENCES e_personal_details(id), FOREIGN KEY(emp_email) REFERENCES e_contact_details(email) )")
conn.execute("CREATE TABLE e_address_details (id INTEGER PRIMARY KEY AUTOINCREMENT, city TEXT, county TEXT, state TEXT, zip INTEGER,region TEXT ,emp_id INTEGER, emp_email TEXT, FOREIGN KEY(emp_id) REFERENCES e_personal_details(id), FOREIGN KEY(emp_email) REFERENCES e_contact_details(email) )")

with open("5000 Records.csv", newline = "") as f:
  reader = csv.reader(f, delimiter=",")
  next(reader)
  number = 1
  for row in reader:
    print(row)

    f_name = row[2]
    l_name = row[3]
    gender = row[5]
    if(row[10][-5] == "-"):
      b_date = datetime.strptime(row[10], '%d-%m-%Y')
    else:
      b_date = datetime.strptime(row[10], '%m/%d/%Y')
    age = float(row[12])
    name_pre = row[1]
    phone_no = row[28]
    email = row[6]
    emergency_phone = fake.phone_number()
    emp_id = number
    number += 1

    cur.execute('INSERT INTO e_personal_details VALUES (NULL,?,?,?,?,?,?)', (f_name, l_name, gender, b_date, age, name_pre))
    cur.execute('INSERT INTO e_contact_details VALUES (NULL,?,?,?,?)', (phone_no, email, emergency_phone, emp_id))
    conn.commit()
    

print("data parsed successfully")
conn.close()




