# BEGIN part 1
# import database module
import copy
import csv
import random
import datetime
import sys

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
    for dictionary in data2.search('login').table:#update value in files csv
        writer.writerow(dictionary.values())
    for dictionary in data2.search('member_pending').table:#update value in files csv
        writer2.writerow(dictionary.values())
    for dictionary in data2.search('project_table').table:#update value in files csv
        writer3.writerow(dictionary.values())
    for dictionary in data2.search('advisor_pending').table:#update value in files csv
        writer4.writerow(dictionary.values())
    myFile.close(), myFile2.close(), myFile3.close(), myFile4.close()

def random_with_N_digits(n):#function to generate project id
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

class student:
    def __init__(self):
        for i in data2.search('member_pending').table:#search for project id in Project_table
            self.id = i['ProjectID']

    def see_pending(self):
        for i in data2.search('member_pending').table:
            if val[0] == i['to_be_member']:
                print(data2.search('member_pending').filter(lambda x: x['to_be_member'] == val[0]))
            elif val[0] != i['to_be_member']:
                print('You have no more invite yet')

    def accept_or_deny(self, a_or_d, id):
        if a_or_d == 'a':
            #accept or deny only project thatt student want
            for i in data2.search('project_table').filter(lambda x: x['ProjectID'] == self.id).table:
                if i['Member1'] == 'None':
                    num = 'Member1'
                elif i['Member1'] != 'None':
                    num = 'Member2'
                else:
                    print('This group is full')
                    sys.exit('')
            data2.search('member_pending').update_row('to_be_member', 'pending', 'to_be_member', 'accepted',
                                                      'to_be_member', val[0])
            data2.search('login').update_row('role', 'student', 'role', 'member', 'ID', val[0])
            data2.search('project_table').update_row(num, 'None', num, val[0], 'ProjectID', id)#num represent a Member1 or 2
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
    def __init__(self):
        for a in data2.search('project_table').filter(lambda x: x['lead'] == val[0]).table:#searh for project id in project_table
            self.id = a['ProjectID']
            self.status = a['status']

    def update(self):
        status = input('what is your progress: ')
        data2.search('project_table').update_row('status', self.status, 'status', status, 'ProjectID', self.id)
        print('project updated')

    def sent(self):
        fac_or_mem = input('want to sent request to be member or to be advisor(member/faculty): ')
        if fac_or_mem == 'member':
            for i in data2.search('project_table').filter(lambda x: x['ProjectID'] == self.id).table:#check if group full or not
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
                    dict_mem = {'ProjectID': self.id, 'to_be_member': st_want, 'Response': 'pending', 'Response_date': '11/11'}
                    data2.search('member_pending').insert_row(dict_mem)
                    print(data2.search('member_pending'))
        elif fac_or_mem == 'faculty':
            for i in data2.search('project_table').filter(lambda x: x['ProjectID'] == self.id).table:#check if group still avarible
                if i['Advisor'] != 'None':
                    print('Your group is full')
                elif i['Advisor'] == 'None':
                    print(data2.search('login').filter(lambda x: x['role'] == 'faculty'))
                    fc_want = int(input('who is faculty you want to invite(id): '))
                    for i in data2.search('advisor_pending').table:
                        if i['to_be_advisor'] == fc_want:
                            print('you already sent an invitation')
                    dict_ad = {'ProjectID': self.id, 'to_be_advisor': fc_want, 'Response': 'pending', 'Response_date': '11/11'}
                    data2.search('advisor_pending').insert_row(dict_ad)
                    print(data2.search('advisor_pending'))

class faculty:
    def __init__(self):
        for i in data2.search('advisor_pending').table:#searh for project id
            self.id = i['ProjectID']

    def see_pending(self):
        for i in data2.search('advisor_pending').table:
            if val[0] == i['to_be_advisor']:
                #print only project that sent invite to this id
                print(data2.search('advisor_pending').filter(lambda x: x['to_be_advisor'] == val[0]))
            elif val[0] != i['to_be_advisor']:
                print('You have no more invite yet')

    def accept_or_deny(self, a_or_d, id):
        if a_or_d == 'a':
            data2.search('advisor_pending').update_row('to_be_advisor', 'pending', 'to_be_advisor', 'accepted', 'ProjectID', id)
            data2.search('login').update_row('role', 'faculty', 'role', 'advisor', 'ID', val[0])
            data2.search('project_table').update_row('Advisor', 'None', 'Advisor', val[0], 'ProjectID', id)
        elif a_or_d == 'd':
            data2.search('advisor_pending').update_row('Response', 'pending', 'Response', 'deny', 'to_be_advisor', val[0])

    def see_detail(self):
        print(data2.search('project_table'))

class advisor:
    def __init__(self):
        for a in data2.search('project_table').filter(lambda x: x['Advisor'] == val[0]).table:#searh for project id
            self.id = a['ProjectID']
            self.status = a['status']

    def update(self):
        status = input('what is your progress: ')
        data2.search('project_table').update_row('status', self.status, 'status', status, 'ProjectID', self.id)
        print('project updated')

    def see(self):
        print(data2.search('project_table').filter(lambda x: x['ProjectID'] == self.id))

    def approve(self, approve):
        if approve == 'yes':
            data2.search('project_table').update_row('status', self.status, 'status', 'approve', 'ProjectID', self.id)
        elif approve == 'no':
            data2.search('project_table').update_row('status', self.status, 'status', 'not_approve', 'ProjectID', self.id)

class member:
    def __init__(self):
        #search for a project id and project status
        for a in data2.search('project_table').filter(lambda x: x['Member1'] == val[0] or x['Member2' == val[0]]).table:
            self.id = a['ProjectID']
            self.status = a['status']

    def see(self):
        print(data2.search('project_table').filter(lambda x: x['ProjectID'] == self.id))

    def update(self):
        status = input('what is your progress')
        data2.search('project_table').update_role('status', self.status, 'status', status, 'ProjectID', self.id)

class admin:
    def __init__(self):
        self.greet = print('hello admin')

    def update(self):
            part = input('which part you want to edit: ')
            if part == 'ID':
                id = input('whose id you want to edit')
                new = input('what is new id')
                data2.search('login').update_row('ID', id, 'ID', new, 'ID', id)
                data2.search('advisor_pending').update_row('to_be_advisor', id, 'to_be_advisor', new, 'to_be_advisor', id)
                data2.search('member_pending').update_row('to_be_member', id, 'to_be_member', new, 'to_be_member', id)
                data2.search('project_table').update_row('lead', id, 'lead', new, 'lead', id)
                data2.search('project_table').update_row('Member1', id, 'Member1', new, 'Member1', id)
                data2.search('project_table').update_row('Member2', id, 'Member2', new, 'Member2', id)
                data2.search('project_table').update_row('Advisor', id, 'Advisor', new, 'Advisor', id)
            elif part == 'Username':
                username = input('what username you want to edit')
                new = input('what is new user name')
                data2.search('login').update_row('username', username, 'username', new, 'username', username)
            elif part == 'password':
                password = input('what password you want to edit')
                new = input('whit is new password')
                data2.search('login').update_row('password', password, 'password', new, 'password', password)
            elif part == 'role':
                new = input('what is new role')
                role = input('what is role you want to edit')
                data2.search('login').update_row('role', role, 'role', new, 'role', role)
            elif part == 'projectid':
                projectid = input('what project you want to edit: ')
                new = input('what is new project id')
                data2.search('project_table').update_row('ProjectID', projectid, 'ProjectID', new, 'ProjectID', projectid)
                data2.search('advisor_pending').update_row('ProjectID', projectid, 'ProjectID', new, 'ProjectID', projectid)
                data2.search('project_pending').update_row('ProjectID', projectid, 'ProjectID', new, 'ProjectID', projectid)
            elif part == 'title':
                title = input('what title you want to edit')
                new = input('what is new project title')
                data2.search('project_table').update_row('Title', title, 'Title', new, 'Title', title)
            elif part == 'status':
                status = input('what is you status of project you want to edit')
                new = input('what is new status')
                data2.search('project_table').update_row('status', status, 'status', new, 'status', status)
            elif part == 'response':
                response = input('what is old response you want to edit')
                new = input('what is new response')
                data2.search('member_pending').update_row('Response', response, 'Response', new, 'Response', response)
                data2.search('advisor_pending').update_row('Response', response, 'Response', new, 'Response', response)
            elif part == 'response_date':
                date = input('what is response date you want to edit')
                new = input('new date')
                data2.search('member_pending').update_row('Response_date', date, 'Response_date', new, 'Response', date)
                data2.search('advisor_pending').update_row('Response_date', date, 'Response_date', new, 'Response', date)

    def see(self):
        part = input('which table you want to see')
        if part == 'Advisor_pending':
            print(data2.search('advisor_pending'))
        elif part == 'Project_table':
            print(data2.search('project_table'))
        elif part == 'Member_pending':
            print(data2.search('member_pending'))
        elif part == 'login':
            print(data2.search('login'))

    def choose(self):
        num = 0
        while num < 3:
            x = data2.search('login').filter(lambda x: x['role'] == 'evaluator').table
            if len(x) == 3:
                print('this project have enough evaluator')
                break
            else:
                print(data2.search('login').filter(lambda x: x['role'] == 'faculty'))
                which = input('who is you choose to be evaluator(id): ')
                data2.search('login').update_row('role', 'faculty', 'role', 'evaluator', 'ID', which)
                num += 1

class evaluator:
    def __init__(self, id):
        self.id = id
        #search for old score
        for x in data2.search('project_table').filter(lambda x: x['ProjectID'] == self.id).table:
            self.old_score = x['status']

    def evaluation(self):
        score = int(input('what score you rate this project (1-10): '))
        #chcek if this project have already rate yet
        if self.old_score != 'approve' or self.old_score != 'not_approve':
            #convert old score to int
            try:
                old = float(self.old_score)
                data2.search('project_table').update_row('status', self.old_score, 'status', str((score + old) / 2),
                                                         'ProjectID', self.id)
            except ValueError:
                print('value erroe')
        elif self.old_score == 'approve':
            data2.search('project_table').update_row('status', 'approve', 'status', str(score), 'ProjectID', self.id)
        elif self.old_score == 'not_approve':
            print('this project is not ready to evaluation')
        data2.search('login').update_row('role', 'evaluator', 'role', 'faculty', 'ID', val[0])








# make calls to the initializing and login functions defined above
data = initializing()
data2 = copy.deepcopy(data)
val = login()
print(val)

# END part 1

# CONTINUE to part 2 (to be done for the next due date)

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id


if val[1] == 'student':
    s = student()
    see_or_edit = input("Want to see a request table or create or accept/deny a project(see/create/accept or deny): ")
    while see_or_edit != 'exit':
        if see_or_edit == 'see':
            s.see_pending()
        elif see_or_edit == 'create':
            ID, name = student.create(val[1])
            dict1 = {'ProjectID': ID, 'Title': name, 'Lead': val[0], 'Member1': 'None', 'Member2': 'None', 'Advisor': 'None', 'status': 'None'}
            data2.search('project_table').insert_row(dict1)
            print(data2.search('project_table'))
            break
        elif see_or_edit == 'accept or deny':
            which = input('which project you want to accept/deny(id): ')
            a_or_d = input('want to accept or deny(a/d): ')
            s.accept_or_deny(a_or_d, which)
        see_or_edit = input('you want to continue or exit(continue or exit): ')

elif val[1] == 'lead':
    l = lead()
    update_or_sent = input('update project or sent a request(update/sent): ')
    while update_or_sent != 'exit':
        if update_or_sent == 'update':
            l.update()
        elif update_or_sent == 'sent':
            l.sent()
        update_or_sent = input('you want to continue or exit(continue/exit): ')

elif val[1] == 'member':
    m = member()
    see_or_update = input('want to see a project table or update project(see/update):  ')
    while see_or_update != 'exit':
        if see_or_update == 'see':
            m.see()
        elif see_or_update == 'edit':
            m.update()
        see_or_update = input('you want to continue or exit(continue/exit): ')

elif val[1] == 'faculty':
    f = faculty()
    what = input(
        'you want to see advisor pending or see project_detail or accept/deny advisor pending(pending/ detail/ a): '
    )
    while what != 'exit':
        if what == 'pending':
            f.see_pending()
        elif what == 'detail':
            f.see_detail()
        elif what == 'a':
            which = input('which project do you want to accept or deny(id): ')
            a_or_d = input('do you accept or deny(a/d): ')
            f.accept_or_deny(a_or_d, which)
            if a_or_d == 'a':
                break
        what = input('you want to continue or exit(continue/exit): ')

elif val[1] == 'advisor':
    a = advisor()
    update_or_see = input('what to update or see project table or approve a project(update/see/approve): ')
    while update_or_see != 'exit':
        if update_or_see == 'see':
            a.see()
        elif update_or_see == 'approve':
            approve = input('is this project approve(yes/no)')
            if approve == 'yes':
                a.approve(approve)
            elif approve == 'no':
                a.approve(approve)
        elif update_or_see == 'update':
            a.update()
        update_or_see = input('what to update or see or exit project table(update/see/approve/exit): ')

elif val[1] == 'admin':
    x = admin()
    see_or_edit = input('you want to see or edit or choose evaluator(see/edit/ choose): ')
    while see_or_edit != 'exit':
        if see_or_edit == 'see':
            x.see()
        elif see_or_edit == 'edit':
            x.update()
        elif see_or_edit == 'choose':
            x.choose()
        see_or_edit = input('you want to see or edit or choose evaluator(see/edit/choose/exit): ')

elif val[1] == 'evaluator':
    print(data2.search('project_table').filter(lambda x: x['status']))
    id = input('which project you want to evaluation: ')
    e = evaluator(id)
    e.evaluation()


exit()
