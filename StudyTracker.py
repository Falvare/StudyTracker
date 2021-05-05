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

    choice = input('option:')

    if choice == '1':
        sessions = 0
        hours = 0
        date = date.today()
        subject = input('please enter subject name:')

        con = sqlite3.connect('subjects.db')
        cur = con.cursor()
        command = '''CREATE TABLE IF NOT EXISTS {} (
                    sessions INTEGER, 
                    hours FLOAT, 
                    date TEXT)'''.format(subject)
        cur.execute(command)

        while True:
            time.sleep(5)
            notification.notify(title=subject, message='your study session has started', timeout=10)
            time.sleep(5)
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
                break

    elif choice == '3':
        break

