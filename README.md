# Adjust Home Task

API for querying performance metrics form DB

## Starting service

- Install requirements
- Copy `config.yaml.example` -> `config.yaml` and fill params (not needed, `config.yaml` provided for time saving)
- Test: `pytest` in project root directory
- Start: `python main.py`

## Service technologies

- Language: *Python 3.9*
- Framework: *FastApi*
- ORM: *Tortoise*
- Database: *SQLite*
- Tests: *PyTest*

## Tasks

1. Show the number of impressions and clicks that occurred before the 1st of June 2017,
broken down by channel and country,sorted by clicks in descending order.
[Click](http://localhost:8080/metrics?date_to=2017-06-01&group_by=channel,country&order_by=-clicks&columns=channel,country,impressions,clicks)  
Query: ```date_to=2017-06-01&group_by=channel,country&order_by=-clicks&columns=channel,country,impressions,clicks```

2. Show the number of installs that occurred in May of 2017 on iOS, broken down by date,
sorted by date in ascending order.
[Click](http://localhost:8080/metrics?date_from=2017-05-01&date_to=2017-05-31&os=ios&order_by=date&group_by=date&columns=date,installs)  
Query: ```date_from=2017-05-01&date_to=2017-05-31&os=ios&order_by=date&group_by=date&columns=date,installs```

3. Show revenue, earned on June 1, 2017 in US, broken down by operating system
and sorted by revenue in descending order.
[Click](http://localhost:8080/metrics?date_from=2017-06-01&date_to=2017-06-01&country=US&group_by=os&order_by=-revenue&columns=os,revenue)  
Query: ```date_from=2017-06-01&date_to=2017-06-01&country=US&group_by=os&order_by=-revenue&columns=os,revenue```

4. Show CPI and spend for Canada (CA), broken down by channel, ordered by CPI in descending order.
Please think carefully which is an appropriate aggregate function for CPI.
[Click](http://localhost:8080/metrics?country=CA&group_by=channel&order_by=-cpi&columns=channel,spend,cpi)  
Query: ```country=CA&group_by=channel&order_by=-cpi&columns=channel,spend,cpi```
