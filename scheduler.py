from apscheduler.schedulers.blocking import BlockingScheduler
from librato_chart_sender.db.config_db import ConfigDB
from librato_chart_sender.interactors import SendChartInteractor
import logging
logging.basicConfig()
logger = logging.getLogger('scheduler_logger')

sched = BlockingScheduler()
@sched.scheduled_job('interval', minutes=1)
def timed_job():
    for config in ConfigDB.get_all_configurations():
        # SendChartInteractor(ConfigDB).run(config.id)
        logger.info('report sent to config_id={config_id}'.format(config_id=config.id))

# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=13)
# def scheduled_job():s
#     print('This job is run every weekday at 5pm.')

sched.start()

