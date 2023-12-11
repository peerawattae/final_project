# BEGIN part 1
# import database module
import copy
import csv

from database import DB, CSV, Table

# define a funcion called initializing

def initializing():
    csv = CSV('persons.csv')
    csv2 = CSV('login.csv')
    csv3 = CSV('Member_pending_request.csv')
    person = csv.open_csv()
    my_db = DB()
    person_table = Table('person', person)
    my_db.insert(person_table)
    logincsv = csv2.open_csv()
    login_table = Table('login', logincsv)
    my_db.insert(login_table)
    member_pending_csv = csv3.open_csv()
    member_pending_table = Table('member_pending', member_pending_csv)
    my_db.insert(member_pending_table)
    return my_db

# here are things to do in this function:

    # create an object to read an input csv file, persons.csv

    # create a 'persons' table

    # add the 'persons' table into the database

    # create a 'login' table

    # the 'login' table has the following keys (attributes):
        # person_id
        # username
        # password
        # role

    # a person_id is the same as that in the 'persons' table

    # let a username be a person's fisrt name followed by a dot and the first letter of that person's last name

    # let a password be a random four digits string

    # let the initial role of all the students be Member

    # let the initial role of all the faculties be Faculty

    # create a login table by performing a series of insert operations; each insert adds a dictionary to a list

    # add the 'login' table into the database

# define a funcion called login

def login():
    data = initializing()
    l = data.search('login')
    print(l)
    username = input('Enter username: ')
    password = input('Enter password: ')
    id_role = []
    for i in l.table:
        if username == i['username'] and password == i['password']:
            id_role.append(i['ID'])
            id_role.append(i['role'])
            return id_role
        else:
            continue

# here are things to do in this function:
   # add code that performs a login task
        # ask a user for a username and password
        # returns [person_id, role] if valid, otherwise returning None


# define a function called exit
def exit():
    with open('login.csv', 'a', newline='') as files:
        writer = csv.DictWriter(files, fieldnames=['ID', 'username', 'password', 'role'])
        # Assuming data2.search('login') returns a dictionary
        data_login = data2.search('login')
        data_login.to_dict()
        writer.writeheader()
        writer.writerow(data_login.to_dict('', ))

    # Writing 'Member_pending_request.csv'
    with open('Member_pending_request.csv', 'a', newline='') as files:
        writer = csv.DictWriter(files, fieldnames=['ProjectID', 'to_be_member', 'Response', 'Response_date'])

        # Assuming data2.search('member_pending') returns a dictionary
        data_member_pending = data2.search('member_pending')
        writer.writeheader()
        writer.writerow(data_member_pending.to_dict('to_be_member', 'pending'))

# here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv files
# By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above
data = initializing()
data2 = copy.deepcopy(data)
val = login()
print(val)

# END part 1

# CONTINUE to part 2 (to be done for the next due date)

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
    # do admin related activities
# elif val[1] = 'advisor':
    # do advisor related activities
# elif val[1] = 'lead':
    # do lead related activities
# elif val[1] = 'member':
    # do member related activities
#elif val[1] = 'faculty':
    # do faculty related activities
a = data.search('login')
k = data.search('member_pending')
if val[1] == 'student':
    see_or_edit = input("Want to see a request table or create a project(see/create): ")
    if see_or_edit == 'see':
        print(data2.search('member_pending'))
        a_or_d = input('want to accept or deny(a/d): ')
        if a_or_d == 'a':
            data2.search('login').update_row('to_be_member', 'pending', 'to_be_member', 'accepted')
            data2.search('member_pending').update_row('role', 'student', 'role', 'member', 'ID', val[0])
        elif a_or_d == 'd':
            data2.search('member_pending').update_row('to_be_member', 'pending', 'to_be_member', 'deny')

    elif see_or_edit == 'create':
        project_name = input("Enter project name: ")
        status = 'lead'
        data2.search('login').update_row('role', 'student', 'role', status, 'ID', val[0])
        print(data2.search('login'))
elif val[1] == 'lead':
    update_or_sent = input('update project or sent a request(update/sent): ')
    if update_or_sent == 'update':
        print('updated')
    elif update_or_sent == 'sent':
        fac_or_mem = input('want to sent request to be member or to be advisor(member/advisor): ')
        if fac_or_mem == 'member':
            data2.search('member_pending').insert_row([{'to_be_member': 'avarible'}])
            data2.search('member_pending').update_row('to_be_member', 'avarible', 'to_be_member', 'pending')
            print(data.search('member_pending'))
        elif fac_or_mem == 'advisor':
            data2.search('').update_row('to_be_advisor', 'avarible', 'to_be_advisor', 'pending')

elif val[1] == 'member':
    see_or_update = input('want to see a project table ')

for i in data2.search('login').table:
    print({'role': i['role']})
