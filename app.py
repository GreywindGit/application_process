from flask import Flask, render_template
import bll

app = Flask(__name__)


menu_items = [('mentors', 'mentors'),
              ('all-school', 'all-school'),
              ('mentors by country', 'mentors-by-country'),
              ('contacts', 'contacts'),
              ('applicants', 'applicants'),
              ('mentors and applicants', 'mentors-and-applicants')]


@app.route('/')
def index():
    return render_template('index.html', menu_items=menu_items)


@app.route('/mentors')
def mentors():
    result_set = bll.get_mentors()
    return render_template('mentors.html', menu_items=menu_items, table=result_set)


if __name__ == '__main__':
    app.run(debug=True)