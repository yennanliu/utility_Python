# python 3 
# DATADOG API PYTHON TEST 
# # https://docs.datadoghq.com/developers/faq/query-the-infrastructure-list-via-the-api/

##########################################################
# load creds 
api_key=your_api_key
application_key=your_application_key
##########################################################

# -------------------------------------------------------------
# TEST 1 
from datadog import initialize, api

options = {'api_key': api_key,
           'app_key': application_key}

initialize(**options)

# -------------------------------------------------------------
# TEST 2 
from datadog import initialize, api
from datadog.api.constants import CheckStatus

options = {'api_key': api_key,
           'app_key': application_key}
initialize(**options)
check = 'app.ok'
host = 'app1'
status = CheckStatus.OK  # equals 0

api.ServiceCheck.check(check=check, host_name=host, status=status,
                       message='Response: 200 OK')

# -------------------------------------------------------------
# TEST 3 

from datadog import initialize, api
initialize(**options)
# Start a new discussion.
# Include a handle like this
api.Comment.create(   
message='Should we use COBOL or Fortran!'
)

# Or set it to None
# and the handle defaults
# to the owner of the application key
api.Comment.create(message='Should we use COBOL or Fortran?')
# Reply to a discussion.
api.Comment.create(  
    message='Smalltalk?',
    related_event_id=23234
)

# -------------------------------------------------------------
# TEST 4 

from datadog import initialize, api
initialize(**options)
api.DashboardList.get_all()

# -------------------------------------------------------------
# TEST 5 

from datadog import initialize, api
import time
initialize(**options)
# Repeat for 3 hours (starting now) on every week day for 4 weeks.
start_ts = int(time.time())
end_ts = start_ts + (3 * 60 * 60)
end_reccurrence_ts = start_ts + (4 * 7 * 24 * 60 * 60)  # 4 weeks from now
recurrence = {
    'type': 'weeks',
    'period': 1,
    'week_days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'until_date': end_reccurrence_ts
}
# Schedule downtime
api.Downtime.create(
    scope='env:staging',
    start=start_ts,
    end=end_ts,
    recurrence=recurrence
)

# -------------------------------------------------------------
# TEST 6 

from datadog import initialize, api
initialize(**options)
# Get all downtimes
print (api.Downtime.get_all())

# -------------------------------------------------------------
# TEST 7 
from datadog import initialize, api
# Intialize request parameters including API/APP key
initialize(**options)
# Call Embed API function
api.Embed.get_all()

# -------------------------------------------------------------
#### TEST 8 ####
# POST AN EVENT 
from datadog import initialize, api
initialize(**options)
title = "test api call4 "
text = 'thisistestapicall4'
tags = ['version:1', 'application:web']
api.Event.create(title=title, text=text, tags=tags)

# -------------------------------------------------------------
# TEST 9 
# DELETE AN EVENT 
from datadog import initialize, api
initialize(**options)
api.Event.delete(4631249271432159157)

# -------------------------------------------------------------
#### TEST 10 #####
# QUERY THE EVENT STREAM 
from datadog import initialize, api
import time
initialize(**options)
end_time = time.time()
start_time = end_time - 100
api.Event.query(
    start=start_time,
    end=end_time,
    priority="normal",
    tags=["application:web"]
    )

# -------------------------------------------------------------
# TEST 11 
# SEARCH HOSTS 
from datadog import initialize, api
initialize(**options)
api.Hosts.search()

# -------------------------------------------------------------
#### TEST 12 ####
# GET LIST OF ACTIVE METRICS 
from datadog import initialize, api
import time
initialize(**options)
# Taking the last 24hours
from_time = int(time.time()) - 60 * 60 * 24 * 1
result = api.Metric.list(from_time)
print(result)

# -------------------------------------------------------------
### TEST 13 ###
# SEARCH METRICS 
from datadog import initialize, api
initialize(**options)
api.Infrastructure.search(q="metrics:system")
