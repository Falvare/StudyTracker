import sqlite3
from plyer import notification
import time
from datetime import date
from pymsgbox import *

option = None

while option != '3':

    print('PLEASE SELECT AN OPTION:')
    print('1.start study session')
    print('2.view stats')
    print('3.quit')
    print('')

    choice = input('option:')

    if choice == '1':
        sessions = 0
        hours = 0
        date = date.today()
        subject = input('please enter subject name:').capitalize()

        con = sqlite3.connect('subjects.db')
        cur = con.cursor()
        command = '''CREATE TABLE IF NOT EXISTS {} (
                    sessions INTEGER, 
                    hours FLOAT, 
                    date TEXT)'''.format(subject)
        cur.execute(command)

        while True:
            print('Your study session will begin in 5 seconds')
            time.sleep(5)
            notification.notify(title=subject, message='your study session has started', timeout=10)
            time.sleep(1800)
            notification.notify(title=subject, message='Your study session has ended. Would you like to continue?',
                                timeout=5)
            sessions += 1
            hours += .5
            con = confirm(text='Your study session has ended. Would you like to continue?', title=subject,
                          buttons=['Yes', 'No'])
            if con == 'Yes':
                continue
            else:
                with sqlite3.connect('subjects.db') as con:
                    cur = con.cursor()
                    command = '''INSERT INTO {} (sessions, hours, date) VALUES (?, ?, ?)'''.format(subject)
                    cur.execute(command, (sessions, hours, date.strftime('%m-%d-%Y')))

                print('')
                print('You have completed ' + str(sessions) + ' total session(s) today')
                print('You have completed ' + str(hours) + ' total hour(s) of study today')
                print('')
                break

    elif choice == '2':
        print('')
        subject = input('What subject would you like to view?').capitalize()

        con = sqlite3.connect('subjects.db')
        cur = con.cursor()
        sessions_cmd = '''SELECT SUM(sessions) FROM {}'''.format(subject)
        hours_cmd = '''SELECT SUM(hours) FROM {}'''.format(subject)
        cur.execute(sessions_cmd)
        total_sessions = cur.fetchone()[0]
        cur.execute(hours_cmd)
        total_hrs = cur.fetchone()[0]
        productive_day_cmd = '''SELECT date, MAX(hours), MAX(sessions) FROM {}'''.format(subject)
        cur.execute(productive_day_cmd)
        productive_day = cur.fetchone()

        print('')
        print('You have completed ' + str(total_sessions) + ' total session(s) for ' + subject)
        print('You have completed ' + str(total_hrs) + ' total hours of study on ' + subject)
        print('Your most productive day was ' + str(productive_day[0]) + ' with ' + str(productive_day[1]) +
              ' total hour(s) and ' + str(productive_day[2]) + ' total sessions completed')
        print('')

    elif choice == '3':
        break
