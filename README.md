# Exam-Scheduler-Cron-Job-for-Exam-Connect
Cron jobs are scheduled at recurring intervals, specified using UNIX-cron format. You can define a schedule so that your job runs multiple times a day, or runs on specific days and months. 


# Exam-Scheduler-Cron-Job-for-Exam-Connect
Cron jobs are scheduled at recurring intervals, specified using the UNIX-cron format. You can define a schedule so that your job runs multiple times a day, or runs on specific days and months. 
For every minute, The cronjob runs to activate the exams which are scheduled in that minute of time.

Here is the Linux command to schedule cronjob

> crontab -e

open ups vim editor


* * * * * python3 /Inueron/firebase-python/examScheduler.py
