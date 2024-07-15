import mysql.connector


config = {
    'user': 'root',
    'password': 'dynamo.6393',
    'host': '127.0.0.1',
    'database': 'futurense'
}



def connect_to_database(config):
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():

            print("Connection successful")
            cursor = connection.cursor()

            return connection
    except mysql.connector.Error as err:

        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")


        else:

            print(err)
    return None

connection = connect_to_database(config)
if connection:
    cursor = connection.cursor()

def login(l_id):
    query = "SELECT * FROM Login WHERE L_id = %s"
    cursor.execute(query, (l_id,))
    result = cursor.fetchone()
    return result

def info(s_id):
    query="SELECT * FROM Student WHERE S_id = %s"
    cursor.execute(query, (s_id,))
    result = cursor.fetchone()
    return result

def coursenroll(s_id):
    query="SELECT C_id FROM Enrollement WHERE S_id = %s"
    cursor.execute(query,(s_id,))
    result = cursor.fetchall()
    l = []
    for i in range(0,len(result)):
        l.append(result[i][0])
    return l

def coursedetail(C_id):
    query = "SELECT * FROM Courses WHERE C_id = %s"
    cursor.execute(query,(C_id,))
    result = cursor.fetchone()
    return result

def get_message(s_id):
    query = "SELECT * FROM Message WHERE S_id = %s"
    cursor.execute(query, (s_id,))
    result = cursor.fetchall()
    return result

def fetch_grades(s_id):
    query = "SELECT * FROM Grades WHERE S_id = %s"
    cursor.execute(query, (s_id,))
    result = cursor.fetchall()
    return result