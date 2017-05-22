from flask import Flask, render_template
import bll

app = Flask(__name__)


menu_items = [('mentors', 'Mentors'),
              ('all-school', 'All School'),
              ('mentors-by-country', 'Mentors by Country'),
              ('contacts', 'Contacts'),
              ('applicants', 'Applicants'),
              ('mentors-and-applicants', 'Mentors and Applicants')]


@app.route('/')
def index():
    return render_template('index.html', menu_items=menu_items)


@app.route('/mentors')
def mentors():
    result_set = bll.get_mentors()
    return render_template('mentors.html', menu_items=menu_items, table=result_set)


@app.route('/all-school')
def all_school():
    result_set = bll.get_all_school()
    return render_template('all-school.html', menu_items=menu_items, table=result_set)


@app.route('/mentors-by-country')
def mentors_by_country():
    result_set = bll.get_mentors_by_country()
    return render_template('mentors-by-country.html', menu_items=menu_items, table=result_set)


if __name__ == '__main__':
    app.run(debug=True)