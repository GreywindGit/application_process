import psycopg2


def establish_connection():
    try:
        connect_str = "dbname='jazmin' user='jazmin' host='localhost' password='correcthorse'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
    except Exception as e:
        print("Cannot connect to database.")
        print(e)
    else:
        return conn


def get_mentors_list():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, last_name FROM mentors ORDER BY first_name, last_name;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_mentor_nicks(city):
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nick_name FROM mentors WHERE city=%s;", (city, ))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def search_by_first_name(name):
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT first_name || ' ' || last_name as full_name, phone_number\
                    FROM applicants WHERE first_name=%s;", (name, ))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def search_by_email(email):
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT first_name || ' ' || last_name as full_name, phone_number\
                    FROM applicants WHERE email LIKE %s;", ('%{}%'.format(email), ))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def add_new_applicant(applicant):
    conn = establish_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO applicants (first_name, last_name, phone_number, email, application_code) \
                        VALUES (%s, %s, %s, %s, %s);", (applicant[0], applicant[1], applicant[2],
                                                        applicant[3], applicant[4]))
        cursor.execute("SELECT * FROM applicants WHERE application_code=%s;", (applicant[4], ))
    except psycopg2.IntegrityError:
        return [("Duplicate application code found. Writing process cancelled.",)]
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def change_applicant_data(updated_applicant):
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE applicants SET phone_number=%s\
                    WHERE first_name=%s AND last_name=%s;", (updated_applicant[2],
                                                             updated_applicant[0], updated_applicant[1]))
    cursor.execute("SELECT first_name || ' ' || last_name as full_name, phone_number FROM applicants\
                    WHERE first_name=%s AND last_name=%s;", (updated_applicant[0], updated_applicant[1]))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows if rows else [("No such applicant in the database", )]


def remove_applicant(domain):
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM applicants WHERE email LIKE %s;", ('%{}'.format(domain), ))
    cursor.close()
    conn.close()
    return [("Applicant(s) removed from the database",)]


def get_unique_attributes(table, attr_name):
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT {} from {};".format(attr_name, table))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
