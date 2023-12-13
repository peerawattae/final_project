# BEGIN part 1
# import database module
import copy
import csv
import random
import datetime

from database import DB, CSV, Table

# define a funcion called initializing

def initializing():
    csv = CSV('persons.csv')
    csv2 = CSV('login.csv')
    csv3 = CSV('Member_pending_request.csv')
    csv4 = CSV('Project_table.csv')
    csv5 = CSV('Advisor_pending_request.csv')
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
    project = csv4.open_csv()
    project_table = Table('project_table', project)
    my_db.insert(project_table)
    advisor = csv5.open_csv()
    advisor_pending = Table('advisor_pending', advisor)
    my_db.insert(advisor_pending)
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
    myFile = open('login.csv', 'w')
    myFile2 = open('Member_pending_request.csv', 'w')
    myFile3 = open('Project_table.csv', 'w')
    myFile4 = open('Advisor_pending_request.csv', 'w')
    writer = csv.writer(myFile)
    writer2 = csv.writer(myFile2)
    writer3 = csv.writer(myFile3)
    writer4 = csv.writer(myFile4)
    writer.writerow(['ID', 'username', 'password', 'role'])
    writer2.writerow(['ProjectID', 'to_be_member', 'Response', 'Response_date'])
    writer3.writerow(['ProjectID', 'Title', 'lead', 'Member1', 'Member2', 'Advisor', 'status'])
    writer4.writerow(['ProjectID', 'to_be_advisor', 'Response', 'Response_date'])
    for dictionary in data2.search('login').table:
        writer.writerow(dictionary.values())
    for dictionary in data2.search('member_pending').table:
        writer2.writerow(dictionary.values())
    for dictionary in data2.search('project_table').table:
        writer3.writerow(dictionary.values())
    for dictionary in data2.search('advisor_pending').table:
        writer4.writerow(dictionary.values())
    myFile.close()

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

class student:
    def __init__(self, id=''):
        self.id = id

    def see(self):
        for i in data2.search('member_pending').table:
            if val[0] == i['to_be_member']:
                print(data2.search('member_pending').filter(lambda x: x['to_be_member'] == val[0]))
            elif val[0] != i['to_be_member']:
                print('You have no more invite yet')
        a_or_d = input('want to accept or deny(a/d): ')
        if a_or_d == 'a':
            for i in data2.search('member_pending').table:
                id = i['ProjectID']
            for i in data2.search('project_table').filter(lambda x: x['ProjectID'] == id).table:
                if i['Member1'] == 'None':
                    num = 'Member1'
                elif i['Member1'] != 'None':
                    num = 'Member2'
            data2.search('member_pending').update_row('to_be_member', 'pending', 'to_be_member', 'accepted', 'to_be_member', val[0])
            data2.search('login').update_row('role', 'student', 'role', 'member', 'ID', val[0])
            data2.search('project_table').update_row(num, 'None', num, val[0], 'ProjectID', id)
        elif a_or_d == 'd':
            data2.search('member_pending').update_row('Response', 'pending', 'Response', 'deny', 'to_be_member', val[0])

    def create(self):
        project_name = input("Enter project name: ")
        status = 'lead'
        data2.search('login').update_row('role', 'student', 'role', status, 'ID', val[0])
        print(data2.search('login'))
        project_id = random_with_N_digits(6)
        return project_id, project_name

class lead:
    def __init__(self, id=''):
        self.id = id

    def update(self):
        for a in data2.search('project_table').filter(lambda x: x['lead'] == val[0]).table:
            id = a['ProjectID']
        status = input('what is your progress: ')
        data2.search('project_table').update_row('status', 'None', 'status', status, 'ProjectID', id)
        print('project updated')

    def sent(self):
        fac_or_mem = input('want to sent request to be member or to be advisor(member/faculty): ')
        for a in data2.search('project_table').filter(lambda x: x['lead'] == val[0]).table:
            id = a['ProjectID']
        if fac_or_mem == 'member':
            for i in data2.search('project_table').filter(lambda x: x['ProjectID'] == id).table:
                if i['Member1'] != 'None' and i['Member2'] != 'None':
                    print('Your group is full')
                elif i['Member1'] == 'None' or i['Member2'] == 'None':
                    print(data2.search('login').filter(lambda x: x['role'] == 'student'))
                    st_want = int(input('who is student you want to invite (id): '))
                    for i in data2.search('member_pending').table:
                        if i['to_be_member'] == st_want:
                            print('you already sent an invitation')
                    status = 'pending'
                    date = datetime
                    dict_mem = {'ProjectID': id, 'to_be_member': st_want, 'Response': 'pending', 'Response_date': '11/11'}
                    data2.search('member_pending').insert_row(dict_mem)
                    print(data2.search('member_pending'))
        elif fac_or_mem == 'faculty':
            for i in data2.search('project_table').filter(lambda x: x['ProjectID'] == id).table:
                if i['Advisor'] != 'None':
                    print('Your group is full')
                elif i['Advisor'] == 'None':
                    print(data2.search('login').filter(lambda x: x['role'] == 'faculty'))
                    fc_want = int(input('who is faculty you want to invite(id): '))
                    for i in data2.search('advisor_pending').table:
                        if i['to_be_advisor'] == fc_want:
                            print('you already sent an invitation')
                    dict_ad = {'ProjectID': id, 'to_be_advisor': fc_want, 'Response': 'pending', 'Response_date': '11/11'}
                    data2.search('advisor_pending').insert_row(dict_ad)
                    print(data2.search('advisor_pending'))

class faculty:
    def __init__(self, id=''):
        self.id = id

    def see(self):
        for i in data2.search('advisor_pending').table:
            if val[0] == i['to_be_advisor']:
                print(data2.search('advisor_pending').filter(lambda x: x['to_be_advisor'] == val[0]))
            elif val[0] != i['to_be_advisor']:
                print('You have no more invite yet')
        a_or_d = input('want to accept or deny(a/d): ')
        if a_or_d == 'a':
            for i in data2.search('advisor_pending').table:
                id = i['ProjectID']
            data2.search('advisor_pending').update_row('to_be_advisor', 'pending', 'to_be_advisor', 'accepted', 'ProjectID', id)
            data2.search('login').update_row('role', 'faculty', 'role', 'advisor', 'ID', val[0])
            data2.search('project_table').update_row('Advisor', 'None', 'Advisor', val[0], 'ProjectID', id)
        elif a_or_d == 'd':
            data2.search('advisor_pending').update_row('Response', 'pending', 'Response', 'deny', 'to_be_advisor', val[0])

class advisor:
    def __init__(self, id=''):
        self.id = id

    def update(self):
        for a in data2.search('project_table').filter(lambda x: x['Advisor'] == val[0]).table:
            id = a['ProjectID']
        status = input('what is your progress: ')
        data2.search('project_table').update_row('status', 'None', 'status', status, 'ProjectID', id)
        print('project updated')


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
if val[1] == 'student':
    see_or_edit = input("Want to see a request table or create a project(see/create): ")
    if see_or_edit == 'see':
        student.see(val[1])
    elif see_or_edit == 'create':
        ID, name = student.create(val[1])
        dict1 = {'ProjectID': ID, 'Title': name, 'Lead': val[0], 'Member1': 'None', 'Member2': 'None', 'Advisor': 'None', 'status': 'None'}
        data2.search('project_table').insert_row(dict1)
        print(data2.search('project_table'))
elif val[1] == 'lead':
    update_or_sent = input('update project or sent a request(update/sent): ')
    if update_or_sent == 'update':
        lead.update(val[1])
    elif update_or_sent == 'sent':
        lead.sent(val[1])

elif val[1] == 'member':
    see_or_update = input('want to see a project table or update project(see/update):  ')

elif val[1] == 'faculty':
    faculty.see(val[1])

elif val[1] == 'advisor':
    advisor.update(val[1])
exit()
