import psycopg2


def establish_connection():
    try:
        connect_str = "dbname='jazmin' user='jazmin' host='localhost' password='correcthorse'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
    except Exception as e:
        print("Ouch, something went wrong...")
        print(e)
    else:
        return conn


def get_mentors_list():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, last_name FROM mentors")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_mentor_nicks():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nick_name FROM mentors WHERE city='Miskolc'")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def search_by_first_name():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT first_name || ' ' || last_name as full_name, phone_number\
                    FROM applicants WHERE first_name='Carol'")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def search_by_email():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT first_name || ' ' || last_name as full_name, phone_number\
                    FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu'")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def add_new_applicant():
    pass


def change_applicant_data():
    pass


def remove_applicant():
    pass



