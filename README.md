# All of my current version of project now in 'main' branch
* how to run
  - Frist you need these following files 1.project_manage.py 2.databse.py 3.login.csv 4.person.csv 5.Project_table 6.Advisor_pending_request.csv 7.Member_pending_request
  - Then when you first run the project_manage.py if you login as a student role the program will ask you if you want to see a member pending request or you want to create a project
  - if you choose create a project you will become a lead otherwise if you choose to see a member_pending request program will ask that you want to join group that sent you invitaion or not
  - if you do accept you will become a member
  - then if you loogin as a lead you can sent invite to a student to be your group member max 2 perseon and can sent a invitaion to a faculty to be you advisor max 1 advisor per group
  - lead can also update project status and see a project status and member of project can also do these feature to
  - if you login as a faculty you can see all project detail and then you can see invite to be advisor you can choose to accept or deny
  - if you accept you will then become a advisor of project
  - advisor can updatae project status see project detail or approve a project to be evaluation
  - admin can see all table and also can edit all of the colum in each table and can choose faculty to be a evaluator
  - when login as a evaluator you will have to grade a project on a scale of 1-10 then program will find a average score of this project
  - then you finish all step
* detail for each files
  -Advisor pending request this files contain a data of a advisor pending contian projectid to_be_advisor Response Response_date
  -Member pending request this files contain a data of a member pending contian projectid to_be_advisor Response Response_date
  -login.csv this files contian a data of each person such as a username id password and role
  -person.csv this files  contian a data of each person such as a fist and last name id and type
  -database.py this files contian a class database class table and class csv
  -project_manage.py this files contain a class student, class lead, class member, class faculty, class advisor, class admin and class evaluator when compile you must compile this files
