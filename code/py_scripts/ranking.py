import mysql.connector

def ranking():
# Connect to the MySQL server
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="university_db",
    )

    # Create a cursor object
    cursor = conn.cursor()


    retrieve_rank_query = """
        SELECT s.name, s.usn, m.CN, m.TOC, m.Java, m.Python, m.IPR
        FROM students s
        JOIN marks m ON s.usn = m.usn
    """

    cursor.execute(retrieve_rank_query)
    result = cursor.fetchall()

    # Process and save the results to files
    count=0
    for row in result:
        name, usn, cn, toc, java, python, ipr = row
        sum=cn + toc + java + python + ipr
        total_marks=(cn + toc + java + python + ipr) 
        if total_marks > 300:
            rank = "Good"
        elif 175 <= total_marks < 300:
            rank = "Average"
        else:
            rank = "Need Improvement"
        
        
        if rank=="Need Improvement":
            count=count+1
            print(count)
        # Create a file with usn.txt and write the report
            with open(f"{usn}.txt", "w") as file:
                file.write(f"Name: {name}, USN: {usn}\n")
                file.write(f"CN: {cn}\n")
                file.write(f"TOC: {toc}\n")
                file.write(f"Java: {java}\n")
                file.write(f"Python: {python}\n")
                file.write(f"IPR: {ipr}\n")
                file.write(f"Total: {sum}\n")
                file.write(f"rank: {rank}")

# Close the connection
    conn.close()

def rank():
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="university_db",
    )

    # Create a cursor object
    cursor = conn.cursor()


    retrieve_rank_query = """
        SELECT  m.CN + m.TOC + m.Java + m.Python + m.IPR as total_marks
        FROM students s
        JOIN marks m ON s.usn = m.usn
    """

    cursor.execute(retrieve_rank_query)
    result = cursor.fetchall()

    ranks=[]

    for row in result:
        total_marks=row[0]
        if int(total_marks) > 300:
            rank = "Good"
        elif 175 <= int(total_marks) < 300:
            rank = "Average"
        else:
            rank = "Need Improvement"
        ranks.append(rank)
        
    return ranks


ranking()

