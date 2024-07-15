import sqlite3

# SQLite database file path
db_file = r"database/futurense.db"

# Function to connect to SQLite database
def connect_to_database():
    try:
        connection = sqlite3.connect(db_file)
        print("Connection to SQLite database successful")
        return connection
    except sqlite3.Error as error:
        print("Error connecting to SQLite database:", error)
        return None

# Connect to SQLite database
connection = connect_to_database()
if connection:
    cursor = connection.cursor()

# Function to retrieve login information by L_id
def login(l_id):
    query = "SELECT * FROM Login WHERE L_id = ?"
    cursor.execute(query, (l_id,))
    result = cursor.fetchone()
    return result

# Function to retrieve student information by S_id
def info(s_id):
    query = "SELECT * FROM Student WHERE S_id = ?"
    cursor.execute(query, (s_id,))
    result = cursor.fetchone()
    return result

# Function to retrieve enrolled courses by S_id
def coursenroll(s_id):
    query = "SELECT C_id FROM Enrollement WHERE S_id = ?"
    cursor.execute(query, (s_id,))
    result = cursor.fetchall()
    return [row[0] for row in result]

# Function to retrieve course details by C_id
def coursedetail(c_id):
    query = "SELECT * FROM Courses WHERE C_id = ?"
    cursor.execute(query, (c_id,))
    result = cursor.fetchone()
    return result

# Function to retrieve messages by S_id
def get_message(s_id):
    query = "SELECT * FROM Message WHERE S_id = ?"
    cursor.execute(query, (s_id,))
    result = cursor.fetchall()
    return result

# Function to retrieve grades by S_id
def fetch_grades(s_id):
    query = "SELECT * FROM Grades WHERE S_id = ?"
    cursor.execute(query, (s_id,))
    result = cursor.fetchall()
    return result