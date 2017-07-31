## Check Crontab Status 

A simple application check status of regular running jobs.
Can modify/add more crontabs by updating crontab.yaml file 

### Quick start 

```
$ cd crontab
$ python check_crontab.py 

```

### Output 

```
1:30 tomorrow /bin/run_me_daily
19:45 today /bin/run_me_hourly
19:16 today /bin/run_me_every_minute
19:16 today /bin/run_me_every_minute
5:16 tomorrow /bin/run_me_xxx

```

with crontab.yaml

```
[30 1 /bin/run_me_daily, 
45 * /bin/run_me_hourly, 
'* * /bin/run_me_every_minute',
'* 19 /bin/run_me_every_minute',
'* 5 /bin/run_me_xxx']
```




