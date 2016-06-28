from apscheduler.schedulers.blocking import BlockingScheduler
from librato_chart_sender.db.config_db import ConfigDB

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    print ConfigDB.get_all_configurations()

# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=13)
# def scheduled_job():
#     print('This job is run every weekday at 5pm.')

sched.start()
