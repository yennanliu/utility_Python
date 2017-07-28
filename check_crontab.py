def get_hour(x):
    try:
        float(x)
        return x 
    except:
        return int(datetime.now().strftime("%H"))
    
def get_minute(x):
    try:
        float(x)
        return x 
    except:
        return int(datetime.now().strftime("%M"))

def get_hr_min(x):
    hour,minute = x.split(" ")[:2][1], x.split(" ")[:2][0]
    #print (hour,minute)
    if hour != '*'  and minute != '*':
        return int(hour) , int(minute)
    if (hour != '*') and (minute == '*'):
        return int(hour), int(datetime.now().strftime("%M"))
    if (hour == '*') and (minute != '*'):
        return int(datetime.now().strftime("%H")),int(minute)
    if (hour == '*') and (minute == '*'):
        return int(datetime.now().strftime("%H")), int(datetime.now().strftime("%M"))


#=============================


def check_cron(cronjobs):
    for cronjob in cronjobs:
        # get current time 
        current = datetime.now().strftime("%H:%M").split(":")
        hour_now,min_now = int(current[0]),int(current[1])
        currenttime= hour_now*60 + min_now 
        # get crontab time 
        hour,minute = get_hr_min(cronjob)
        crontime = int(minute) + int(hour)*60
        if currenttime - crontime > 0:
            print (hour,':',minute,'tomorrow',cronjob.split(" ")[2])
        if currenttime - crontime < 0:
            print (hour,':',minute ,'today',cronjob.split(" ")[2])
        if currenttime - crontime == 0:
            print (hour_now,':',min_now,'now',cronjob.split(" ")[2])

                               
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



                               