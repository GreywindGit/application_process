import os
import dal
import bll


def menu():
    menu_items = ["List of mentors", "Nicknames of mentors in a city", "Search applicant's phone number by first name",
                  "Search applicant by e-mail address", "Add new applicant", "Change applicant's phone number",
                  "Remove applicant(s) by domain", "Exit program"]
    menu_choice = 0
    while menu_choice not in range(1, len(menu_items)+1):
        os.system('clear')
        for index, item in enumerate(menu_items):
            print('{}) {}'.format(index+1, item))
        try:
            menu_choice = int(input("\nChoose a menu item: "))
        except ValueError:
            menu_choice = 0
    if menu_choice == 1:
        header = 'Mentors'
        table = dal.get_mentors_list()
    elif menu_choice == 2:
        city = bll.get_city()
        header = 'Nicknames of mentors in {}'.format(city)
        table = dal.get_mentor_nicks(city)
    elif menu_choice == 3:
        name = bll.get_first_name()
        header = '{}\'s phone number'.format(name)
        table = dal.search_by_first_name(name)
    elif menu_choice == 4:
        email = bll.get_email()
        header = 'Phone number of applicant(s) by (partial) e-mail "{}"'.format(email)
        table = dal.search_by_email(email)
    elif menu_choice == 5:
        applicant = bll.get_new_applicant()
        header = 'New applicant'
        table = dal.add_new_applicant(applicant)
    elif menu_choice == 6:
        updated_applicant = bll.get_changing_applicant()
        header = 'Updated applicant data'
        table = dal.change_applicant_data(updated_applicant)
    elif menu_choice == 7:
        domain = bll.get_domain()
        header = ''
        table = dal.remove_applicant(domain)
    else:
        pass
    if menu_choice != 8:
        display_table(table, header)
        restart()


def display_table(table, header=''):
    os.system('clear')
    if header:
        print(header)
        max_row_length = max([len(' '.join([str(data) for data in item])) for item in table])
        separator = max_row_length if max_row_length > len(header) else len(header)
        print('-' * separator)
    for row in table:
        for item in row:
            print(item, end=' ')
        print()
    print()


def restart():
    input('Press Enter to continue... ')
    menu()


if __name__ == '__main__':
    menu()
