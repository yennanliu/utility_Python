

from datetime import datetime


def get_hr_min(x):
    # get hour, minute from crontab
    hour,minute = x.split(" ")[:2][1], x.split(" ")[:2][0]
    current_hr, current_min = datetime.now().strftime("%H"), datetime.now().strftime("%M")
    # if crontab once in specific time, return crontab runtime 
    if hour != '*'  and minute != '*':
        return int(hour) , int(minute)
    # if crontab run once every hour, return crontab hour and current time minute
    if (hour != '*') and (minute == '*'):
        return int(hour), int(current_min)
    # if crontab run once hourly in specific minute , return crontab minute and current time hour
    if (hour == '*') and (minute != '*'):
        return int(current_hr),int(minute)
    # if crontab run once every minute, return current hour and current minute 
    if (hour == '*') and (minute == '*'):
        return int(current_hr), int(current_min)


def check_cron(cronjobs):
    for cronjob in cronjobs:
        # get current time 
        current = datetime.now().strftime("%H:%M").split(":")
        hour_now,min_now = int(current[0]),int(current[1])
        currenttime= hour_now*60 + min_now 
        # get crontab time 
        hour,minute = get_hr_min(cronjob)
        cron_content = cronjob.split(" ")[2]
        crontime = int(minute) + int(hour)*60
        if currenttime - crontime > 0:
            yield '{}:{} tomorrow {}'.format(hour,minute,cron_content)
        if currenttime - crontime < 0:
            yield '{}:{} today {}'.format(hour,minute,cron_content)
        if currenttime - crontime == 0:
            yield '{}:{} today {}'.format(hour_now,min_now,cron_content)
 

#=============================

def pipeline(cronjobs):
    pipeline_ = check_cron(cronjobs)     
    for cron in pipeline_:
        print (cron)



                      
#=============================
"""

myluist=['30 1 /bin/run_me_daily',
 '45 * /bin/run_me_hourly',
 '* * /bin/run_me_every_minute',
 '* 19 /bin/run_me_sixty_times']

mylist2=['30 19 /bin/run_me_daily',
 '45 * /bin/run_me_hourly',
 '* * /bin/run_me_every_minute',
 '* 19 /bin/run_me_sixty_times']


"""
#=============================



                               