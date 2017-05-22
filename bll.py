import dal


def get_mentors():
    sql_string = "SELECT mentors.first_name, mentors.last_name, schools.name, schools.country\
                  FROM mentors\
                  JOIN schools ON mentors.city = schools.city\
                  ORDER BY mentors.id;"
    result_set = dal.get_data_from_table(sql_string)
    return result_set
