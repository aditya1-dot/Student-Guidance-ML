import mysql.connector
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ranking import ranking,rank
from automail import send_email
import subprocess
import time
# Function to generate random email addresses
def generate_email(usn, domain):
    return f"{usn.lower()}.{domain}"

# Function to generate random names
def generate_name():
    first_names = ["John", "Jane", "Bob", "Alice", "Charlie", "Eve", "David", "Emma", "Frank", "Grace"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Connect to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="university_db",
)

# Create a cursor object
cursor = conn.cursor()

students = []
marks_data = []  

for i in range(1, 11):
    usn = f"1nt21cs{i:03d}"
    name = generate_name()
    semester = 5
    student_email = generate_email(usn, "nmit.ac.in")
    # print(type(student_email))
    # student_email="1nt21cs198.venkatesh@nmit.ac.in","1nt21cs198.venkatesh@nmit.ac.in","1nt21cs198.venkatesh@nmit.ac.in","1nt21cs198.venkatesh@nmit.ac.in","1nt21cs198.venkatesh@nmit.ac.in","1nt21cs198.venkatesh@nmit.ac.in","1nt21cs198.venkatesh@nmit.ac.in","1nt21cs198.venkatesh@nmit.ac.in","1nt21cs198.venkatesh@nmit.ac.in","1nt21cs198.venkatesh@nmit.ac.in"
    # student_email = ",".join(student_email)    
    parents_email = f"parent{i}@gmail.com"

    students.append((usn, name, semester, parents_email, student_email))

    # Generate random marks for each subject (assuming out of 100)
    marks = [random.randint(20,50 ) for _ in range(5)]
    marks_data.append((usn, *marks))  # Use a different variable for marks data

# Insert data into the 'students' table
insert_student_query = "INSERT INTO students (usn, name, semester, parents_email, student_email) VALUES (%s, %s, %s, %s, %s)"
cursor.executemany(insert_student_query, students)

# Insert data into the 'marks' table
insert_marks_query = "INSERT INTO marks (usn, CN, TOC , Java, Python, IPR) VALUES (%s, %s, %s, %s, %s, %s)"
cursor.executemany(insert_marks_query, marks_data)  # Use the correct variable

# Commit the changes and close the connection
conn.commit()
conn.close()

ranking()

ranks=rank()
for r in ranks:
    if r == "Need Improvement":
        send_email("Invitation to Performance Review Session", "Dear Student , \n I hope this email finds you well. As part of our commitment to your academic success, we would like to invite you to a personalized performance review session to discuss your progress and address any concerns or questions you may have \n Follow the link given below (http://192.168.141.153:8501) \n Ps. This is an automated mail.", "1nt21ad004.aditya@nmit.ac.in")



command="streamlit run /Users/adityasinha/Desktop/PROJECT/setmax/PythonFile/code/main.py"
subprocess.run(command,shell=True)




