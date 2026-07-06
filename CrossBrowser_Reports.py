#30-06-2026

#Cross browser testing:
# in conftest file do this modification for cross browser testing


'''@pytest.fixture(params=['chrome','edge','firefox'])
def setup_and_teardown(request):
    parameter= request.param

    if parameter == 'chrome':
        driver = webdriver.Chrome()
    elif parameter == 'edge':
        driver = webdriver.Edge()
    elif parameter == 'firefox':
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    yield driver
    driver.quit()'''
from selenium.webdriver.common.devtools.v143.target import activate_target

#Genearting HTML Reports:

# pytest-html plugin is used to generate HTML reports

# goto project framework & enter in terminal:
'''   pip install pytest-html '''

#To get reports generate: goto project framework and Enter:
'''   python -m pytest -vs --html=report1.html'''

#To create HTML report in new file use this command:
''' python -m pytest -vs --html=reports/report2.html'''


#To create virtual Environment:
#Goto terminal
'''python -m venv venv
venv\Scripts\activate
install selenium
install pytest-dependency'''


#dependency is in test_Markers.py in pyTest folder

#reports are in Demo_Tricentis_Framework


#02-07-2026

# Version Control:
# It is a system to store the version of ur project
#--> Instead of creating multiple copies, Git store the changes

#Advantages:
#--> Backup of project
#--> Keep history (all changes done)
#--> Restore old version
#--> Track changes made
#--> Team collaboration

#GIT:
# It is a distributed version control system
#--> It stores every version of project in our own computer, it works locally
#GIT--> local

#GITHUB: It is a cloud platform that stores git repositories online
#--> Stores cloud

#after installing git
#open cmd enter:
# git --version ---> to check git is installed properly

'''git config --global user.name "Name"
git config --global user.email "emailID"
git config --list # To verify all details entered in git
'''

#Structure:
#working directory--> it is folder where we create files
'''git add'''
#staging area--> It is like waiting room
'''git commit'''
#Local repository
'''git push'''
# #GitHub repository


#create git_demo folder in project: enter all the below commands

'''git init'''   # --> Initialize empty git repository
#--> Git create a hidden folder .git--> stores all the history

'''git status''' # --> Check the current condition/status of the repository

#we need to add file inside Git_demo directory ex: demo1.py
'''# git add .
     git add filename(demo1.py)'''  #--> the file gets moved to staging area

#Use git add . everytime after changes made to file (to save changes)

'''git commit -m "first commit"'''  #where commit--> save version,
# -m -->message,
# First commit--> description

'''git log''' #--> it gives view history, commit ID, Author, data and message
#every commit will have unique ID

#sign up GitHub:
#create repository and copy the path/URL
#then come to pycharm:
# git remote add origin https://github.com/pavan143200/GitDemo.git
# git branch -M main
# git push -u origin main

#to PULL: goto github, open file-- click edit--make changes
# come to pycharm enter git pull

#04-07-2026
#To work with Jenkins we should download java

# goto chrome : enter java 21 and select oracle.com URL
# select JDK 21 windows
# then click 64 installer
# download JDK 21 and install it
#goto c: program files, select java folder--jdk21--bin copy URL
#search bar goto env variables, path, new-- paste link--ok

#goto chrome: enter jenkins, click download select windows option
#make changes by selecting path as java/jdk 21 install it and finish

#goto chrome: enter localhost 8080



#06-07-2026
#create file.text and enter selenium,pytest,pytest-html,openpyxl
'''pip install -r requirements.txt'''

#create file name with Jenkinsfile and add plugins like Jenkins syntax highlighter and
#   goto settings click on plugins in market place to install plugin
# copypaste code from trainer in Jenkinsfile and edit the python path in file

#To find python path: goto cmd enter:
'''where python'''

#push framework to github
#make pages edit login_page, test_login remove from demotricentis.pages

#open jenkins--click new item-- give name--select pipeline--ok
#  select pipeline copy url from github(goto project code) and paste it

