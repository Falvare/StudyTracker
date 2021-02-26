import os
import time
from datetime import date
from plyer import notification

# Change the directory to the folder where you would like to save your study tracker document
os.chdir(r'C:\Users\19156\Desktop\python\Study Tracker')


def timer(study, brk):
    study = study * 60
    brk = brk * 60
    time.sleep(5)
    notification.notify(title='Begin', message='Your study session has started')
    time.sleep(study)
    notification.notify(title='Break time', message='take a break')
    time.sleep(brk)


sbj = input('What are you studying?:')
sbj_file = sbj.capitalize() + '.txt'

hours = 0
sessions = 0

choice = 1
while choice != sessions:
    print('Your study session will begin in 5 seconds')
    timer(30, 5)
    notification.notify(title='Continue',
                        message='You have completed your study session(s). Would you like to continue?')
    sessions = sessions + 1
    if sessions == sessions + 2:
        hours = hours + 1
    else:
        hours = hours + .5
    cont = input('Would you like to continue?:').capitalize()
    if cont == 'Yes':
        choice = choice + 1
        continue
    elif cont == 'No':
        break

notification.notify(title='Congratulations!', message='You have completed your study sessions for today')

today = str(date.today())

if not os.path.exists(sbj_file):
    with open(sbj_file, 'x') as subject:
        subject.write('DATE:')
        subject.write(today)
        subject.write('\n')
        subject.write('SESSIONS:')
        subject.write(str(sessions))
        subject.write('\n')
        subject.write('HOURS:')
        subject.write(str(hours))
        subject.write('\n')
        subject.write('\n')
else:
    with open(sbj_file, 'a') as subject:
        subject.write('DATE:')
        subject.write(today)
        subject.write('\n')
        subject.write('SESSIONS:')
        subject.write(str(sessions))
        subject.write('\n')
        subject.write('HOURS:')
        subject.write(str(hours))
        subject.write('\n')
        subject.write('\n')

session_lst = []
hours_lst = []

with open(sbj_file, 'r') as subject:
    for line in subject:
        if line.startswith('SESSIONS:'):
            line = line.split(':')
            sess = int(line[1])
            session_lst.append(sess)
        elif line.startswith('HOURS:'):
            line = line.split(':')
            hrs = float(line[1])
            hours_lst.append(hrs)

total_hrs = str(sum(hours_lst))
total_sessions = str(sum(session_lst))

print('You have completed', sessions, 'sessions today')
print('You have completed', hours, 'hours today')
print('You have', total_hrs, 'total hours of study on', sbj)
print('you have', total_sessions, 'total', sbj, 'study sessions')
