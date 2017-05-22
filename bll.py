import dal


def get_mentors():
    sql_string = "SELECT mentors.first_name, mentors.last_name, schools.name, schools.country\
                  FROM mentors\
                  JOIN schools ON mentors.city = schools.city\
                  ORDER BY mentors.id;"
    result_set = dal.get_data_from_table(sql_string)
    return result_set


def get_all_school():
    sql_string = "SELECT mentors.first_name, mentors.last_name, schools.name, schools.country\
                  FROM mentors\
                  FULL JOIN schools ON mentors.city = schools.city\
                  ORDER BY mentors.id;"
    result_set = dal.get_data_from_table(sql_string)
    return result_set


def get_mentors_by_country():
    sql_string = "SELECT schools.country, count(mentors.id)\
                  FROM mentors\
                  JOIN schools ON mentors.city = schools.city\
                  GROUP BY schools.country\
                  ORDER BY schools.country;"
    result_set = dal.get_data_from_table(sql_string)
    return result_set


def get_contacts():
    sql_string = "SELECT schools.name, mentors.first_name, mentors.last_name\
                  FROM schools\
                  LEFT JOIN mentors ON schools.contact_person = mentors.id\
                  ORDER BY schools.name;"
    result_set = dal.get_data_from_table(sql_string)
    return result_set
