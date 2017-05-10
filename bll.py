import dal
from random import randint


def get_city():
    CITIES = (''.join(item) for item in dal.get_unique_attributes('mentors', 'city'))
    city = input("Which city's mentors would you like to see? ")
    if city not in CITIES:
        city = 'Miskolc'
    return city


def get_first_name():
    FIRST_NAMES = (''.join(item) for item in dal.get_unique_attributes('applicants', 'first_name'))
    first_name = input("Whose phone number are you looking for? ")
    if first_name not in FIRST_NAMES:
        first_name = 'Carol'
    return first_name


def get_email():
    EMAILS = (''.join(item) for item in dal.get_unique_attributes('applicants', 'email'))
    email = input("What is the e-mail of the applicant? (You can enter partial e-mail address.) ")
    for item in EMAILS:
        if email in item and len(email) > 0:
            return email
    email = '@adipiscingenimmi.edu'
    return email


def generate_application_code():
    APP_CODES = (item[0] for item in dal.get_unique_attributes('applicants', 'application_code'))
    new_app_code = 0
    while new_app_code in APP_CODES or new_app_code == 0:
        new_app_code = randint(10000, 99999)
    return new_app_code


def get_new_applicant():
    FIELDS = ('first name', 'last name', 'phone number', 'e-mail')
    new_applicant = list()
    for item in FIELDS:
        new_applicant.append(input("New applicant's {}: ".format(item)))
    if all([item == '' for item in new_applicant]):
        return ['Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823]
    new_applicant.append(generate_application_code())
    return new_applicant


def get_changing_applicant():
    FIELDS = ('first name', 'last name', 'new phone number')
    changing_applicant = list()
    for item in FIELDS:
        changing_applicant.append(input("Applicant's {}: ".format(item)))
    if all([item == '' for item in changing_applicant]):
        return ['Jemima', 'Foreman', '003670/223-7459']
    return changing_applicant


def get_domain():
    EMAILS = (''.join(item) for item in dal.get_unique_attributes('applicants', 'email'))
    domain = input("Domain name to look for: ")
    if len(domain) == 0:
        return '@mauriseu.net'
    domain = '@' + domain
    return domain
