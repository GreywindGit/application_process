from flask import Flask, render_template
import bll

app = Flask(__name__)


menu_items = [('mentors', 'Mentors'),
              ('all-school', 'All School'),
              ('mentors-by-country', 'Mentors by Country'),
              ('contacts', 'Contacts'),
              ('applicants', 'Applicants'),
              ('applicants-and-mentors', 'Mentors and Applicants')]


@app.route('/')
def index():
    return render_template('index.html', menu_items=menu_items, main_page=True)


@app.route('/mentors')
def mentors():
    active_item = 'mentors'
    table_header = ['First name', 'Last name', 'School', 'Country']
    result_set = bll.get_mentors()
    return render_template('mentors.html', menu_items=menu_items, active_item=active_item,
                           table_header=table_header, table=result_set)


@app.route('/all-school')
def all_school():
    active_item = 'all-school'
    table_header = ['First name', 'Last name', 'School', 'Country']
    result_set = bll.get_all_school()
    return render_template('all-school.html', menu_items=menu_items, active_item=active_item,
                           table_header=table_header, table=result_set)


@app.route('/mentors-by-country')
def mentors_by_country():
    active_item = 'mentors-by-country'
    table_header = ['Country', '# of mentors']
    result_set = bll.get_mentors_by_country()
    return render_template('mentors-by-country.html', menu_items=menu_items, active_item=active_item,
                           table_header=table_header, table=result_set)


@app.route('/contacts')
def get_contacts():
    active_item = 'contacts'
    table_header = ['School', 'First name', 'Last name']
    result_set = bll.get_contacts()
    return render_template('contacts.html', menu_items=menu_items, active_item=active_item,
                           table_header=table_header, table=result_set)


@app.route('/applicants')
def get_applicants():
    active_item = 'applicants'
    table_header = ['First name', 'Application Code', 'Date of Application']
    result_set = bll.get_applicants()
    return render_template('applicants.html', menu_items=menu_items, active_item=active_item,
                           table_header=table_header, table=result_set)


@app.route('/applicants-and-mentors')
def get_applicants_n_mentors():
    active_item = 'applicants-and-mentors'
    table_header = ['Applicant\'s name', 'Application Code', 'Mentor\'s first name', 'Mentor\'s last name']
    result_set = bll.get_applicants_n_mentors()
    return render_template('applicants-and-mentors.html', menu_items=menu_items, active_item=active_item,
                           table_header=table_header, table=result_set)


if __name__ == '__main__':
    app.run(debug=True)