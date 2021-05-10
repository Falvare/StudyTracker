# StudyTracker 

This is a command line study timer that will keep a log of your study sessions and give you an overview after each session. 

Each study session is 30 minutes long. This program will notify you after your 30 minute study session is over and a messgaebox will populate asking if you would like to continue studying. If you would like to begin another 30 minute study session select 'Yes', otherwise selct 'No'. 

Once you are finished studying, it will search the SQLITE3 database for a table with the name of subject you entered into the program. If there is no table by that name, it will be created and log the date, number of sessions completed, and the total hours completed. If there is already a table by that name, it will add add that information to the existing table. Once the session information is written to the database, the program will give you the number of blocks and hours that you did this session.

Users will also have the option to view their stats for a subject by selecting option number 2. If the subject entered is not in the databse, you will be asked if you would like to add it. If 'Yes' is selected, a new table will be created for that subject, otherwise you will be prompted to enter another subject. If the subject is in the database, it will tell you the total number of sessions, hours studied, and the date with the most study sessions completed. 
