import os
import dal


def menu():
    menu_items = ["List of mentors", "Nicknames of mentors in Miskolc", "Search applicant Carol's phone number",
                  "Search applicant by e-mail address", "New applicant", "Change applicant's data",
                  "Remove an applicant", "Exit program"]
    menu_choice = 0
    while menu_choice not in range(1, len(menu_items)+1):
        os.system('clear')
        for index, item in enumerate(menu_items):
            print('{}) {}'.format(index+1, item))
        try:
            menu_choice = int(input("Choose a menu item: "))
        except ValueError:
            menu_choice = 0
    if menu_choice == 1:
        header = 'Mentors'
        table = dal.get_mentors_list()
    elif menu_choice == 2:
        header = 'Nicknames of mentors in Miskolc'
        table = dal.get_mentor_nicks()
    elif menu_choice == 3:
        header = 'Carol\'s phone number'
        table = dal.search_by_first_name()
    elif menu_choice == 4:
        header = 'Applicant\'s phone number'
        table = dal.search_by_email()
    elif menu_choice == 5:
        header = 'New applicants'
        table = dal.add_new_applicant()
    elif menu_choice == 6:
        header = 'Updated applicant data'
        table = dal.change_applicant_data()
    elif menu_choice == 7:
        header = ''
        table = dal.remove_applicant()
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
    input_key = ''
    while input_key != 'c':
        input_key = input('Press c to continue...')
    menu()


if __name__ == '__main__':
    menu()
